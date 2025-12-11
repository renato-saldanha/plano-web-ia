"use client";

import { useEffect, useRef, useState } from "react";

type Message = { id: string; role: "user" | "assistant"; content: string };

const API_BASE = "http://localhost:8000"; // ajuste se necessário
const ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc2ODAwNjg0MiwidHlwZSI6ImFjY2VzcyJ9.wP_yG1lOz0QdzkqA6ObTKhZBuUttMoq8c7Kz8mv2D-w";

async function streamSSE(
  url: string,
  body: unknown,
  onChunk: (text: string) => void
) {
  const res = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${ACCESS_TOKEN}`,
    },
    body: JSON.stringify(body),
  });

  if (!res.body) throw new Error("Resposta sem corpo");

  const reader = res.body.getReader();
  const decoder = new TextDecoder("utf-8");

  let buffer = "";
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    buffer += decoder.decode(value, { stream: true });
    const parts = buffer.split("\n\n");
    buffer = parts.pop() ?? "";
    for (const part of parts) {
      if (!part.startsWith("data:")) continue;
      const text = part.replace(/^data:\s?/, "");
      if (text === "[DONE]") return;
      if (text.length) onChunk(text);
    }
  }
}

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: "welcome",
      role: "assistant",
      content: "Olá! Sou seu agente. Envie uma mensagem que eu respondo.",
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const viewportRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    viewportRef.current?.scrollTo({
      top: viewportRef.current.scrollHeight,
      behavior: "smooth",
    });
  }, [messages]);

  const handleSend = async () => {
    const text = input.trim();
    if (!text || loading) return;

    const userMsg: Message = {
      id: crypto.randomUUID(),
      role: "user",
      content: text,
    };
    const assistantId = crypto.randomUUID();
    const assistantMsg: Message = {
      id: assistantId,
      role: "assistant",
      content: "",
    };

    setMessages((prev) => [...prev, userMsg, assistantMsg]);
    setInput("");
    setLoading(true);

    try {
      await streamSSE(
        `${API_BASE}/api/generate`,
        { prompt: text, model: "gpt-4o-mini" },
        (chunk) => {
          setMessages((prev) =>
            prev.map((m) =>
              m.id === assistantId
                ? { ...m, content: (m.content || "") + chunk }
                : m
            )
          );
        }
      );
    } catch (err) {
      setMessages((prev) =>
        prev.map((m) =>
          m.id === assistantId
            ? { ...m, content: "[erro ao obter resposta]" }
            : m
        )
      );
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (event: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="flex min-h-screen justify-center bg-zinc-50 px-4 py-8 font-sans text-zinc-900 dark:bg-black dark:text-zinc-50">
      <main className="flex h-full w-full max-w-4xl flex-col rounded-2xl border border-zinc-200 bg-white shadow-sm dark:border-zinc-800 dark:bg-zinc-900">
        <header className="flex items-center justify-between border-b border-zinc-200 px-6 py-4 dark:border-zinc-800">
          <div>
            <p className="text-sm font-semibold text-emerald-500">Chat • SSE</p>
            <h1 className="text-xl font-semibold">Agente Assistente</h1>
          </div>
          <span className="rounded-full bg-emerald-500/10 px-3 py-1 text-xs font-medium text-emerald-600">
            {loading ? "Respondendo..." : "Online"}
          </span>
        </header>

        <section
          ref={viewportRef}
          className="flex flex-1 flex-col gap-3 overflow-y-auto px-6 py-6"
        >
          {messages.map((message) => (
            <div
              key={message.id}
              className={`w-full rounded-2xl px-4 py-3 text-sm leading-relaxed shadow-sm ${
                message.role === "assistant"
                  ? "bg-emerald-50 text-emerald-900 dark:bg-emerald-900/30 dark:text-emerald-50"
                  : "bg-zinc-100 text-zinc-900 dark:bg-zinc-800 dark:text-zinc-50"
              }`}
            >
              <div className="mb-1 text-[11px] uppercase tracking-wide text-zinc-500 dark:text-zinc-400">
                {message.role === "assistant" ? "Agente" : "Você"}
              </div>
              <p className="whitespace-pre-wrap">{message.content}</p>
            </div>
          ))}
        </section>

        <footer className="border-t border-zinc-200 bg-zinc-50/80 px-6 py-4 dark:border-zinc-800 dark:bg-zinc-900/80">
          <div className="flex items-end gap-3">
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Digite sua pergunta... (Enter envia, Shift+Enter quebra a linha)"
              rows={3}
              className="h-[92px] min-h-[92px] w-full resize-none rounded-xl border border-zinc-200 bg-white px-3 py-3 text-sm leading-relaxed text-zinc-900 shadow-inner outline-none transition focus:border-emerald-500 focus:ring-2 focus:ring-emerald-200 dark:border-zinc-800 dark:bg-zinc-950 dark:text-zinc-50 dark:focus:border-emerald-400 dark:focus:ring-emerald-900"
              style={{ maxHeight: "10.5rem", overflowY: "auto" }}
              disabled={loading}
            />
            <button
              type="button"
              onClick={handleSend}
              className="mb-1 inline-flex h-[46px] items-center justify-center rounded-xl bg-emerald-600 px-4 text-sm font-semibold text-white shadow-sm transition hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-emerald-300 disabled:cursor-not-allowed disabled:bg-emerald-400"
              disabled={!input.trim() || loading}
            >
              Enviar
            </button>
          </div>
          <p className="mt-2 text-xs text-zinc-500 dark:text-zinc-400">
            O campo aceita scroll até ~7 linhas; use Shift+Enter para quebra de
            linha.
          </p>
        </footer>
      </main>
    </div>
  );
}
