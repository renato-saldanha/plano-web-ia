# 🛡️ Guia: Tratamento de Exceções com pdfplumber

## 📚 Exceções Comuns do pdfplumber

O pdfplumber pode lançar várias exceções. Aqui estão as principais:

1. **FileNotFoundError** - Arquivo não encontrado
2. **PermissionError** - Sem permissão para ler o arquivo
3. **PDFSyntaxError** - PDF corrompido ou inválido
4. **Exception genérica** - Outros erros

---

## ✅ Exemplo 1: Tratamento Básico (Melhorado)

### ❌ Código Atual (com problemas):
```python
def extrair_texto_pdf(caminho_pdf: str) -> str:
    try:
        pdf_file = pdfplumber.open(caminho_pdf)
        pdf_text = ""
        for page in pdf_file.pages:
            pdf_text += page.extract_text() + '\n'   
        print({pdf_text})  # ❌ Erro: chaves ao invés de parênteses
        return pdf_text
    except Exception as e:
        print(f"Erro ao extrair texto do PDF: {e}")
        # ❌ Problema: não retorna None, não fecha o arquivo
```

### ✅ Código Corrigido:
```python
from typing import Optional
import pdfplumber

def extrair_texto_pdf(caminho_pdf: str) -> Optional[str]:
    """
    Extrai texto de um arquivo PDF.
    
    Args:
        caminho_pdf: Caminho para o arquivo PDF
    
    Returns:
        String com o texto extraído ou None em caso de erro
    """
    try:
        # Usar 'with' para garantir que o arquivo seja fechado
        with pdfplumber.open(caminho_pdf) as pdf:
            texto_completo = ""
            
            for pagina in pdf.pages:
                texto_pagina = pagina.extract_text()
                if texto_pagina:  # Verificar se não é None
                    texto_completo += texto_pagina + "\n"
            
            return texto_completo.strip()
            
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {caminho_pdf}")
        return None
        
    except PermissionError:
        print(f"❌ Sem permissão para ler o arquivo: {caminho_pdf}")
        return None
        
    except Exception as e:
        print(f"❌ Erro ao extrair texto do PDF: {e}")
        return None
```

**Melhorias:**
- ✅ Usa `with` para fechar arquivo automaticamente
- ✅ Trata exceções específicas
- ✅ Retorna `None` em caso de erro
- ✅ Verifica se `extract_text()` retorna `None`

---

## ✅ Exemplo 2: Tratamento Detalhado

```python
from typing import Optional
import pdfplumber
import os

def extrair_texto_pdf(caminho_pdf: str) -> Optional[str]:
    """
    Extrai texto de um arquivo PDF com tratamento completo de erros.
    
    Args:
        caminho_pdf: Caminho para o arquivo PDF
    
    Returns:
        String com o texto extraído ou None em caso de erro
    """
    # Validação prévia
    if not caminho_pdf:
        print("❌ Caminho do PDF não fornecido")
        return None
    
    if not os.path.exists(caminho_pdf):
        print(f"❌ Arquivo não existe: {caminho_pdf}")
        return None
    
    if not caminho_pdf.lower().endswith('.pdf'):
        print(f"⚠️  Aviso: Arquivo não tem extensão .pdf: {caminho_pdf}")
    
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            texto_completo = ""
            total_paginas = len(pdf.pages)
            
            print(f"📄 Processando PDF com {total_paginas} página(s)...")
            
            for i, pagina in enumerate(pdf.pages, start=1):
                try:
                    texto_pagina = pagina.extract_text()
                    
                    if texto_pagina:
                        texto_completo += f"\n--- Página {i} ---\n"
                        texto_completo += texto_pagina + "\n"
                    else:
                        print(f"⚠️  Página {i} não contém texto extraível")
                        
                except Exception as e:
                    print(f"⚠️  Erro ao extrair texto da página {i}: {e}")
                    continue  # Continua com próxima página
            
            if not texto_completo.strip():
                print("⚠️  Nenhum texto foi extraído do PDF")
                return None
            
            print(f"✅ Texto extraído com sucesso ({len(texto_completo)} caracteres)")
            return texto_completo.strip()
            
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {caminho_pdf}")
        print("   Verifique se o caminho está correto")
        return None
        
    except PermissionError:
        print(f"❌ Sem permissão para ler o arquivo: {caminho_pdf}")
        print("   O arquivo pode estar aberto em outro programa")
        return None
        
    except pdfplumber.exceptions.PDFSyntaxError as e:
        print(f"❌ PDF corrompido ou inválido: {caminho_pdf}")
        print(f"   Erro: {e}")
        return None
        
    except Exception as e:
        print(f"❌ Erro inesperado ao processar PDF: {e}")
        print(f"   Tipo de erro: {type(e).__name__}")
        return None
```

---

## ✅ Exemplo 3: Tratamento com Informações Detalhadas

```python
from typing import Optional, Dict, Any
import pdfplumber
import os

def extrair_texto_pdf_com_info(caminho_pdf: str) -> Optional[Dict[str, Any]]:
    """
    Extrai texto de PDF e retorna informações detalhadas.
    
    Args:
        caminho_pdf: Caminho para o arquivo PDF
    
    Returns:
        Dicionário com texto e metadados, ou None em caso de erro:
        {
            "texto": str,
            "total_paginas": int,
            "total_caracteres": int,
            "paginas_com_texto": int,
            "erros": list
        }
    """
    resultado = {
        "texto": "",
        "total_paginas": 0,
        "total_caracteres": 0,
        "paginas_com_texto": 0,
        "erros": []
    }
    
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            resultado["total_paginas"] = len(pdf.pages)
            
            for i, pagina in enumerate(pdf.pages, start=1):
                try:
                    texto_pagina = pagina.extract_text()
                    
                    if texto_pagina and texto_pagina.strip():
                        resultado["texto"] += f"\n--- Página {i} ---\n"
                        resultado["texto"] += texto_pagina + "\n"
                        resultado["paginas_com_texto"] += 1
                    else:
                        resultado["erros"].append(f"Página {i}: sem texto")
                        
                except Exception as e:
                    erro_msg = f"Página {i}: {str(e)}"
                    resultado["erros"].append(erro_msg)
                    continue
            
            resultado["texto"] = resultado["texto"].strip()
            resultado["total_caracteres"] = len(resultado["texto"])
            
            if resultado["total_caracteres"] == 0:
                return None
                
            return resultado
            
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {caminho_pdf}")
        return None
        
    except PermissionError:
        print(f"❌ Sem permissão para ler: {caminho_pdf}")
        return None
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return None
```

---

## ✅ Exemplo 4: Função Completa com Type Hints

```python
from typing import Optional
import pdfplumber
import os

def extrair_texto_pdf(caminho_pdf: str) -> Optional[str]:
    """
    Extrai texto de um arquivo PDF usando pdfplumber.
    
    Args:
        caminho_pdf: Caminho completo ou relativo para o arquivo PDF
    
    Returns:
        String com todo o texto extraído do PDF, ou None em caso de erro
    
    Raises:
        Não levanta exceções, sempre retorna None em caso de erro
    
    Example:
        >>> texto = extrair_texto_pdf("documento.pdf")
        >>> if texto:
        ...     print(f"Texto extraído: {len(texto)} caracteres")
    """
    # Validação inicial
    if not caminho_pdf or not caminho_pdf.strip():
        print("❌ Caminho do PDF não fornecido")
        return None
    
    # Verificar se arquivo existe
    if not os.path.exists(caminho_pdf):
        print(f"❌ Arquivo não encontrado: {caminho_pdf}")
        return None
    
    # Verificar se é um arquivo (não diretório)
    if not os.path.isfile(caminho_pdf):
        print(f"❌ Caminho não é um arquivo: {caminho_pdf}")
        return None
    
    try:
        # Abrir PDF com context manager (fecha automaticamente)
        with pdfplumber.open(caminho_pdf) as pdf:
            texto_completo = ""
            total_paginas = len(pdf.pages)
            
            if total_paginas == 0:
                print("⚠️  PDF não contém páginas")
                return None
            
            # Extrair texto de cada página
            for i, pagina in enumerate(pdf.pages, start=1):
                try:
                    texto_pagina = pagina.extract_text()
                    
                    # extract_text() pode retornar None
                    if texto_pagina:
                        texto_completo += texto_pagina + "\n"
                    else:
                        print(f"⚠️  Página {i}/{total_paginas}: sem texto extraível")
                        
                except Exception as e:
                    # Erro ao processar uma página específica
                    print(f"⚠️  Erro na página {i}/{total_paginas}: {e}")
                    continue  # Continua com próxima página
            
            # Verificar se extraiu algum texto
            texto_final = texto_completo.strip()
            
            if not texto_final:
                print("⚠️  Nenhum texto foi extraído do PDF")
                return None
            
            print(f"✅ Extraído {len(texto_final)} caracteres de {total_paginas} página(s)")
            return texto_final
            
    except FileNotFoundError:
        # Arquivo foi deletado entre a verificação e a abertura
        print(f"❌ Arquivo não encontrado: {caminho_pdf}")
        return None
        
    except PermissionError:
        # Sem permissão para ler o arquivo
        print(f"❌ Sem permissão para ler: {caminho_pdf}")
        print("   Dica: O arquivo pode estar aberto em outro programa")
        return None
        
    except pdfplumber.exceptions.PDFSyntaxError as e:
        # PDF corrompido ou formato inválido
        print(f"❌ PDF corrompido ou inválido: {caminho_pdf}")
        print(f"   Detalhes: {e}")
        return None
        
    except Exception as e:
        # Qualquer outro erro
        print(f"❌ Erro inesperado ao processar PDF: {e}")
        print(f"   Tipo: {type(e).__name__}")
        return None
```

---

## 🔍 Tipos de Exceções do pdfplumber

### 1. **FileNotFoundError** (built-in Python)
```python
except FileNotFoundError:
    # Arquivo não existe no caminho especificado
```

### 2. **PermissionError** (built-in Python)
```python
except PermissionError:
    # Sem permissão para ler o arquivo
    # Pode estar aberto em outro programa
```

### 3. **PDFSyntaxError** (pdfplumber específica)
```python
import pdfplumber

try:
    # código
except pdfplumber.exceptions.PDFSyntaxError:
    # PDF corrompido ou formato inválido
```

### 4. **Exception genérica**
```python
except Exception as e:
    # Captura qualquer outro erro
    # Útil para debug: print(type(e).__name__)
```

---

## 💡 Dicas Importantes

### 1. **Sempre use `with` statement**
```python
# ✅ BOM - Fecha automaticamente
with pdfplumber.open(caminho) as pdf:
    # processar

# ❌ RUIM - Pode não fechar
pdf = pdfplumber.open(caminho)
# processar
# Esqueceu de fechar!
```

### 2. **Verifique se `extract_text()` retorna None**
```python
texto = pagina.extract_text()
if texto:  # ✅ Sempre verificar
    # usar texto
```

### 3. **Trate erros por página**
```python
for pagina in pdf.pages:
    try:
        texto = pagina.extract_text()
    except Exception as e:
        # Erro em uma página não deve parar o processo
        continue
```

### 4. **Validações prévias**
```python
# Verificar antes de abrir
if not os.path.exists(caminho):
    return None

if not caminho.endswith('.pdf'):
    print("Aviso: não é .pdf")
```

---

## 🎯 Exemplo Final: Código Completo para seu Dia 4

```python
from typing import Optional
import pdfplumber
import os

def extrair_texto_pdf(caminho_pdf: str) -> Optional[str]:
    """
    Extrai texto de um arquivo PDF.
    
    Args:
        caminho_pdf: Caminho para o arquivo PDF
    
    Returns:
        String com o texto extraído ou None em caso de erro
    """
    # Validação
    if not caminho_pdf or not os.path.exists(caminho_pdf):
        print(f"❌ Arquivo não encontrado: {caminho_pdf}")
        return None
    
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            texto_completo = ""
            
            for pagina in pdf.pages:
                texto_pagina = pagina.extract_text()
                if texto_pagina:
                    texto_completo += texto_pagina + "\n"
            
            return texto_completo.strip() if texto_completo.strip() else None
            
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {caminho_pdf}")
        return None
    except PermissionError:
        print(f"❌ Sem permissão para ler: {caminho_pdf}")
        return None
    except Exception as e:
        print(f"❌ Erro ao extrair texto: {e}")
        return None
```

---

## 📚 Referências

- [pdfplumber Documentation](https://github.com/jsvine/pdfplumber)
- [Python Exception Handling](https://docs.python.org/3/tutorial/errors.html)

