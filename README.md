# Aira — Local AI Voice Assistant

Aira is a **local, privacy-focused AI voice assistant** built with Python and open-source AI technologies.

The goal of Aira is to create a capable personal assistant that can understand natural speech, process requests using a locally running LLM, execute controlled system tasks, maintain conversational context, and respond naturally through voice.

The project follows an **offline-first, modular, low-latency, and extensible architecture**.

---

## ✨ Features

- 🎙️ Voice-based interaction
- 🗣️ Speech recognition using Faster-Whisper
- 🧠 Local LLM inference using Ollama
- 🔊 Local text-to-speech using Piper
- 🎧 Voice Activity Detection using Silero VAD
- ⚡ Direct PCM audio streaming for low-latency TTS
- 💬 Short-term conversation memory
- 🕐 Date and time utilities
- 🖥️ Application launching
- 🌐 Basic browser and web operations
- 🔎 Google and YouTube search
- 🔒 Offline-first architecture
- 🧩 Modular tool-based architecture

---

## 🏗️ Current Architecture

```
                ┌──────────────┐
                │  Microphone  │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │    FFmpeg    │
                │ Audio Capture│
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │  Silero VAD  │
                │Speech Detect │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │Faster-Whisper│
                │     STT      │
                └──────┬───────┘
                       ↓
              ┌───────────────────┐
              │ Task Handler / LLM│
              └─────────┬─────────┘
                        ↓
                ┌──────────────┐
                │   Response   │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │    Piper     │
                │     TTS      │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │    FFplay    │
                └──────┬───────┘
                       ↓
                    🔊 Speaker
```

---

## 🚀 Work Completed

### 1. Speech-to-Text

Aira uses **Faster-Whisper** for local speech recognition.

Implemented functionality:
- Local Whisper inference
- Automatic language detection
- Speech-to-text conversion
- Detected language information
- Language probability information
- Modular STT implementation

The STT component is separated from the main application so that the speech-recognition model can be changed independently.

### 2. Voice Activity Detection

Aira uses **Silero VAD** to detect when the user starts and stops speaking.

Recording pipeline:

```
Microphone → FFmpeg → Audio Chunks → Silero VAD → Speech Detected → Speech Ended → Audio Returned
```

Implemented functionality:
- Real-time microphone capture
- Chunk-based audio processing
- Speech probability detection
- Configurable speech threshold
- Silence detection
- Speech termination
- Pre-buffering before speech detection

Current recording configuration:

| Setting | Value |
|---|---|
| Sample Rate | 16000 Hz |
| Channels | Mono |
| Chunk Size | 512 |
| Speech Threshold | 0.5 |
| Pre-buffer | Enabled |
| Silence Detection | Enabled |

### 3. Local LLM

Aira uses **Ollama** for local LLM inference.

- Current model: `llama3.2:3b`
- Ollama API: `http://localhost:11434/api/generate`

The LLM handles normal conversational interactions and receives the current conversation history. The assistant prompt is designed to:
- Respond in English by default
- Understand minor speech-to-text mistakes
- Maintain conversational context
- Avoid inventing real-time information
- Keep spoken responses concise
- Ask for clarification when necessary
- Avoid unnecessary formatting
- Never claim an action was performed when it was not

### 4. Conversation History

Aira currently maintains short-term conversation history during an active session.

Example:

```
User: What is Python?
Aira: Python is a programming language...

User: Who created it?
Aira: Python was created by Guido van Rossum.
```

Conversation history is stored in memory and passed to the local LLM. Persistent long-term memory is planned for a future phase.

### 5. Text-to-Speech

Aira uses **Piper TTS** for local speech synthesis.

- Current voice: `en_US-lessac-medium`
- Voice model: `voices/en_US-lessac-medium.onnx`

The current TTS pipeline uses direct PCM streaming:

```
Piper → PCM Audio Chunks → FFplay stdin → Speaker
```

No temporary WAV file is required. This avoids unnecessary disk I/O and reduces response latency.

### 6. Audio Processing

Aira uses **FFmpeg** and **FFplay** for audio input and output.

**FFmpeg** is used for:
- Microphone capture
- Audio format conversion
- PCM audio streaming
- Feeding audio into the VAD pipeline

**FFplay** is used for:
- Local audio playback
- Playing Piper-generated PCM audio
- Receiving audio through standard input

The TTS system directly streams generated audio to FFplay instead of creating an intermediate audio file.

### 7. Task Execution

Aira currently has a deterministic task-handler layer for system operations.

**Date and Time** — Aira can handle current time, current date, current day, and current date and time. The date/time utilities use the `Asia/Kolkata` timezone.

**Application Launching** — Aira contains a separate application layer for opening supported applications, with definitions maintained independently from the main application.

**Browser and Web Operations** — Current capabilities include:
- Open Google
- Open YouTube
- Open YouTube in Brave
- Google search
- YouTube search

These operations are currently handled through deterministic task logic.

---

## 📁 Project Structure

```
AI-Assistant/
│
├── app.py
│
├── speech/
│   ├── speech_to_text.py
│   ├── recorder.py
│   ├── vad.py
│   └── Text_to_speech.py
│
├── llm/
│   └── ollama_client.py
│
├── tools/
│   ├── task_handler.py
│   ├── date_time.py
│   ├── applications.py
│   └── web_tools.py
│
├── voices/
│   ├── en_US-lessac-medium.onnx
│   └── en_US-lessac-medium.onnx.json
│
├── requirements.txt
│
└── README.md
```

The project follows a modular structure where each component has a specific responsibility:

| File | Responsibility |
|---|---|
| `speech_to_text.py` | Speech Recognition |
| `vad.py` | Voice Activity Detection |
| `recorder.py` | Audio Recording |
| `Text_to_speech.py` | Text-to-Speech |
| `ollama_client.py` | LLM Communication |
| `date_time.py` | Date/Time Tools |
| `applications.py` | Application Control |
| `web_tools.py` | Web Operations |

---

## 🧰 Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Speech-to-Text | Faster-Whisper |
| Voice Activity Detection | Silero VAD |
| LLM Runtime | Ollama |
| Current LLM | Llama 3.2 3B |
| Text-to-Speech | Piper |
| Audio Processing | FFmpeg |
| Audio Playback | FFplay |
| Numerical Processing | NumPy |
| ML Runtime | PyTorch |
| Environment | Conda |
| Development Platform | Ubuntu on WSL |

---

## 📦 Installation

### 1. Create Conda Environment

```bash
conda create -n aira python=3.12
conda activate aira
```

### 2. Install FFmpeg

```bash
sudo apt update
sudo apt install ffmpeg
```

Verify the installation:

```bash
ffmpeg -version
ffplay -version
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Install Ollama and make sure the Ollama server is running.

Download the current model:

```bash
ollama pull llama3.2:3b
```

Verify:

```bash
ollama list
```

### 5. Add Piper Voice

Place the Piper voice model inside `voices/`. Required files:

```
voices/
├── en_US-lessac-medium.onnx
└── en_US-lessac-medium.onnx.json
```

---

## ▶️ Running Aira

Activate the environment:

```bash
conda activate aira
```

Navigate to the project:

```bash
cd /mnt/c/Users/randhir/Desktop/Projects/Aira/AI-Assistant
```

Run:

```bash
python app.py
```

Aira should display:

```
==================================================
        AIRA AI ASSISTANT
==================================================
Aira is ready!
Speak naturally. Say 'exit' or 'bye' to stop.
==================================================
```

The assistant will then wait for voice input. To stop Aira, say **"bye"** or **"exit"**.

---

## 🧪 Example Interaction

```
Aira is ready!

🎤 Speak Now...

Listening....
Speech detected....
Speech Ended....

You: What is machine learning?

Language: en

A: Machine learning is a branch of artificial intelligence...
```

The generated response is then converted into speech using Piper.

---

## 🔐 Design Principles

**Offline First**
```
Speech → Local STT → Local LLM → Local TTS
```
This minimizes dependence on external AI APIs.

**Privacy**
The long-term goal is to keep normal conversations and AI processing on the local machine wherever practical.

**Modular Architecture**
Instead of one huge file with everything mixed together, Aira follows:
```
STT → VAD → Recorder → LLM → Tools → TTS
```
This makes individual components easier to test, debug, replace, and improve.

**Low Latency**
Aira avoids unnecessary intermediate processing. TTS does not use `Piper → WAV File → Disk → FFplay`; instead it uses `Piper → PCM Audio → FFplay → Speaker`, reducing unnecessary disk I/O and improving response latency.

**Safe Tool Execution**
Aira should not provide unrestricted shell or Python execution to the LLM. System capabilities will instead be exposed through explicitly defined and controlled tools.

---

## 🗺️ Future Roadmap

The next major goal is to evolve Aira from a keyword-based task assistant into an LLM-driven local AI agent.

### Phase 1 — Core Voice Assistant ✅ Completed
- [x] Microphone audio capture
- [x] FFmpeg audio pipeline
- [x] Silero VAD
- [x] Speech detection
- [x] Silence detection
- [x] Speech pre-buffering
- [x] Faster-Whisper STT
- [x] Local Ollama LLM
- [x] Conversation history
- [x] Piper TTS
- [x] Direct PCM TTS streaming
- [x] FFplay audio playback
- [x] Date/time utilities
- [x] Application launching
- [x] Basic browser operations
- [x] Google search
- [x] YouTube search

### Phase 2 — LLM Tool Calling

This is the next major architectural upgrade. Currently, task selection is largely based on keyword and pattern matching:

```
User: "What time is it?" → Keyword Matching → get_current_time() → Result
```

The future architecture will allow the LLM itself to decide which tool should be used:

```
User Speech → STT → LLM Agent → Tool Selection
                                      ↓
                        ┌───────────────────────┐
                        │ Available Tools       │
                        │ get_time()            │
                        │ get_date()            │
                        │ open_app()            │
                        │ search_google()       │
                        │ search_youtube()      │
                        │ open_url()            │
                        │ find_file()           │
                        │ etc.                  │
                        └───────────┬───────────┘
                                    ↓
                          Tool Execution → Tool Result → LLM → Final Response → TTS
```

Planned work:
- [ ] Tool schemas
- [ ] Tool registry
- [ ] LLM function/tool calling
- [ ] Structured tool arguments
- [ ] Tool argument validation
- [ ] Tool execution layer
- [ ] Tool result handling
- [ ] Tool error handling
- [ ] Whitelisted tools
- [ ] Remove unnecessary keyword-based routing

### Phase 3 — System Tools

Aira will gain more useful computer-control capabilities.

Planned tools:
- [ ] Open applications
- [ ] Close applications safely
- [ ] Open folders
- [ ] Search files
- [ ] Find files
- [ ] Read files
- [ ] Create files
- [ ] Rename files
- [ ] Move files
- [ ] Copy files
- [ ] Search directories
- [ ] System information

All system operations will be implemented as controlled tools.

### Phase 4 — Browser Agent

The current browser functionality will evolve into a more capable browser agent.

Planned capabilities:
- [ ] Web search
- [ ] Website navigation
- [ ] Search result extraction
- [ ] Web page summarization
- [ ] Browser automation
- [ ] Multi-step browser tasks
- [ ] LLM-driven web tool selection

Example flow:
```
User: "Find the latest research paper on MLIPs and summarize the important points."
→ LLM Agent → Web Search Tool → Research Paper → Content Extraction → LLM → Summary → TTS
```

### Phase 5 — Persistent Memory

Currently, Aira only maintains conversation history during the current session. Future versions will support persistent long-term memory.

Target architecture:
```
Conversation → Memory Extraction → Embeddings → Vector Database → Persistent Memory
```

During future conversations:
```
User Query → Memory Retrieval → Relevant Memories → LLM Context → Response
```

Planned features:
- [ ] Long-term memory
- [ ] User preferences
- [ ] Important facts
- [ ] Conversation summaries
- [ ] Semantic memory search
- [ ] Memory retrieval
- [ ] Memory deletion
- [ ] Memory correction

### Phase 6 — Streaming and Performance

Aira will eventually move toward a more responsive real-time pipeline.

Current: `User speaks → Complete STT → Complete LLM response → TTS → Audio`

Future: `User speaks → Streaming STT → LLM starts generating → First sentence available → TTS starts → Speaker`

Planned improvements:
- [ ] Streaming STT
- [ ] Streaming LLM output
- [ ] Sentence-level TTS
- [ ] Parallel processing
- [ ] Lower first-response latency
- [ ] GPU acceleration
- [ ] Better interruption handling

### Phase 7 — Continuous Conversation

Aira should eventually support natural back-and-forth conversations without needing to restart listening manually.

Planned improvements:
- [ ] Continuous listening mode
- [ ] Automatic turn detection
- [ ] Better silence handling
- [ ] User interruption
- [ ] Aira interruption
- [ ] Conversation state management

### Phase 8 — Wake Word

Wake-word functionality will be revisited after the core agent architecture is stable.

Target behavior: `Background → "Aira" → Assistant Activates → User Speaks → Aira Responds → Back to Waiting`

Planned work:
- [ ] Evaluate pretrained wake-word models
- [ ] Custom wake-word model
- [ ] Natural speech dataset
- [ ] False-positive testing
- [ ] Background-noise testing
- [ ] Continuous low-power detection

### Phase 9 — Vision

Future versions may support visual input.

Potential capabilities:
- [ ] Screenshot understanding
- [ ] Screen analysis
- [ ] Camera input
- [ ] Visual question answering
- [ ] Screen-aware assistance
- [ ] Visual computer interaction

### Phase 10 — Documents and RAG

Aira may eventually become capable of working with local documents.

Target architecture:
```
Documents → Chunking → Embeddings → Vector Database → Relevant Retrieval → LLM → Answer
```

Planned capabilities:
- [ ] PDF question answering
- [ ] Document summarization
- [ ] Local document search
- [ ] Embedding generation
- [ ] Vector database
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Personal knowledge base

### Phase 11 — Productivity Assistant

Long-term productivity capabilities may include:
- [ ] Calendar integration
- [ ] Email integration
- [ ] Reminders
- [ ] Task management
- [ ] Notes
- [ ] Personal scheduling
- [ ] Notification handling

---

## 🧠 Long-Term Agent Architecture

The final architecture is expected to evolve toward:

```
                         ┌──────────────┐
                         │  Microphone  │
                         └──────┬───────┘
                                ↓
                         ┌──────────────┐
                         │     VAD      │
                         └──────┬───────┘
                                ↓
                         ┌──────────────┐
                         │     STT      │
                         │ FasterWhisper│
                         └──────┬───────┘
                                ↓
                       ┌─────────────────┐
                       │    LLM Agent    │
                       │                 │
                       │ Reasoning       │
                       │ Planning        │
                       │ Tool Selection  │
                       └────────┬────────┘
                                ↓
                 ┌──────────────┴──────────────┐
                 ↓                             ↓
          ┌──────────────┐              ┌──────────────┐
          │    Tools     │              │    Memory    │
          │              │              │              │
          │ System       │              │ Short-term   │
          │ Browser      │              │ Long-term    │
          │ Files        │              │ Semantic     │
          │ Web          │              │              │
          └──────┬───────┘              └──────┬───────┘
                 ↓                             ↓
                 └──────────────┬──────────────┘
                                ↓
                         ┌──────────────┐
                         │   Response   │
                         └──────┬───────┘
                                ↓
                         ┌──────────────┐
                         │     TTS      │
                         │    Piper     │
                         └──────┬───────┘
                                ↓
                            🔊 Speaker
```

---

## 📈 Development Roadmap

```
                    CURRENT
                       │
                       ▼
              ┌─────────────────┐
              │ Core Voice      │
              │ Pipeline        │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ LLM Tool Calling│
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ System Tools    │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Browser Agent   │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Persistent      │
              │ Memory          │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Streaming &     │
              │ Performance     │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Wake Word       │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Vision + RAG    │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Personal AI     │
              │ Agent           │
              └─────────────────┘
```

---

## 🧪 Development Philosophy

Aira is being developed incrementally. Each capability follows:

```
Design → Implement → Test Independently → Integrate → Test with Real Voice Interaction → Refactor → Move to Next Capability
```

The project intentionally avoids building one huge monolithic assistant. Instead:

```
One Capability → One Module → One Clear Responsibility
```

This makes the project easier to debug, maintain, test, and extend.

---

## 🎯 Final Vision

The long-term goal of Aira is to build a fully local personal AI agent capable of:

- Understanding natural speech
- Maintaining conversational context
- Reasoning using a local LLM
- Selecting tools automatically
- Safely interacting with the computer
- Searching and understanding information
- Remembering useful information
- Working with local documents
- Understanding visual information
- Performing multi-step tasks
- Responding naturally through voice
- Operating primarily without cloud AI services

The intended evolution:

```
Voice Assistant → Conversational Assistant → Tool-Using Assistant → Local AI Agent → Personal AI System
```

---

## 📌 Current Development Priority

```
Stable Voice Pipeline
        ↓
LLM Tool Calling
        ↓
Modular System Tools
        ↓
Browser Agent
        ↓
Persistent Memory
        ↓
Streaming / Performance
        ↓
Wake Word
        ↓
Vision + RAG
        ↓
Advanced Personal Agent
```

Aira is under active development, and the architecture will continue to evolve as better local models, tools, and techniques are evaluated.

---

## 👨‍💻 Project

**Aira — Local AI Voice Assistant**

Built with Python, open-source AI models, and a modular architecture.

> Build locally. Think intelligently. Act safely.
