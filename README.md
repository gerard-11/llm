# Asistente de escritura automática

Proyecto 1 del módulo de LLM. Es una aplicación web construida con Streamlit que utiliza la API de OpenAI para apoyar tres tareas de escritura:

1. Mejorar redacción y ortografía.
2. Sugerir la continuación de un texto.
3. Generar un texto desde cero con un tono seleccionado.

## Requisitos

- Python 3.8 o superior.
- Una clave de API de OpenAI.

La clave nunca se guarda en el repositorio. La aplicación puede recibirla mediante la variable de entorno `OPENAI_API_KEY` o solicitarla en la interfaz.

## Instalación

Desde la carpeta del proyecto:

```bash
cd asistente_escritura
python -m venv venv
source venv/bin/activate
```

En Windows PowerShell, activa el entorno con:

```powershell
venv\Scripts\Activate.ps1
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Linux o macOS:

```bash
export OPENAI_API_KEY="tu_clave_de_openai"
streamlit run app.py
```

Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="tu_clave_de_openai"
streamlit run app.py
```

También puedes ejecutar `streamlit run app.py` sin definir la variable y escribir la clave directamente en la aplicación.

El modelo utilizado por defecto es `gpt-4.1-mini`. Puedes cambiarlo definiendo la variable opcional `OPENAI_MODEL`.

## Estructura

```text
asistente_escritura/
├── app.py
└── requirements.txt
```

## Tecnologías

- Python
- Streamlit
- OpenAI Responses API
