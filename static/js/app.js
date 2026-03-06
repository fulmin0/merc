'use strict';

const messagesEl = document.getElementById('messages');
const inputEl = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendBtn');
const voiceBtn = document.getElementById('voiceBtn');
const chatContainer = document.getElementById('chatContainer');
const headerStatus = document.getElementById('headerStatus');

let conversationId = 'session-' + Date.now();
let isProcessing = false;
let recognition = null;
let isListening = false;

// ── Helpers ──────────────────────────────────────────────────────────────────

function scrollToBottom() {
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

function formatTime() {
  return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function formatMessage(text) {
  return escapeHtml(text)
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    .replace(/`(.*?)`/g, '<code>$1</code>')
    .replace(/\n/g, '<br>');
}

function setStatus(text, cls = '') {
  headerStatus.textContent = text;
  headerStatus.className = 'header-status ' + cls;
}

// ── Messages ─────────────────────────────────────────────────────────────────

function addMessage(role, text) {
  const div = document.createElement('div');
  div.className = 'message ' + role;
  div.innerHTML = `<div class="message-bubble">${formatMessage(text)}</div>`;
  messagesEl.appendChild(div);
  scrollToBottom();
  return div;
}

function showTyping() {
  const div = document.createElement('div');
  div.className = 'message assistant typing-indicator';
  div.id = 'typing';
  div.innerHTML = `<div class="message-bubble"><div class="typing-dots"><span></span><span></span><span></span></div></div>`;
  messagesEl.appendChild(div);
  scrollToBottom();
}

function removeTyping() {
  const el = document.getElementById('typing');
  if (el) el.remove();
}

// ── Send message ──────────────────────────────────────────────────────────────

async function sendMessage() {
  const text = inputEl.value.trim();
  if (!text || isProcessing) return;

  inputEl.value = '';
  autoResize(inputEl);
  isProcessing = true;
  sendBtn.disabled = true;
  setStatus('Thinking...', 'thinking');

  addMessage('user', text);
  showTyping();

  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text, conversation_id: conversationId }),
    });

    const data = await res.json();
    removeTyping();

    if (res.ok && data.response) {
      addMessage('assistant', data.response);
    } else {
      addMessage('assistant', '⚠️ ' + (data.detail || 'Something went wrong.'));
    }
  } catch {
    removeTyping();
    addMessage('assistant', '⚠️ Connection error. Is the server running?');
  }

  isProcessing = false;
  sendBtn.disabled = false;
  setStatus('Ready');
  inputEl.focus();
}

function sendQuick(text) {
  inputEl.value = text;
  sendMessage();
}

function handleKeydown(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
}

function autoResize(el) {
  el.style.height = 'auto';
  el.style.height = Math.min(el.scrollHeight, 120) + 'px';
}

// ── Voice input ───────────────────────────────────────────────────────────────

function setupVoice() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    voiceBtn.classList.add('unsupported');
    voiceBtn.title = 'Voice not supported in this browser';
    return;
  }

  recognition = new SpeechRecognition();
  recognition.continuous = false;
  recognition.interimResults = true;
  recognition.lang = 'en-US';

  recognition.onstart = () => {
    isListening = true;
    voiceBtn.classList.add('listening');
    inputEl.placeholder = 'Listening...';
    setStatus('Listening...', 'thinking');
  };

  recognition.onresult = (e) => {
    const transcript = Array.from(e.results).map(r => r[0].transcript).join('');
    inputEl.value = transcript;
    autoResize(inputEl);
  };

  recognition.onend = () => {
    isListening = false;
    voiceBtn.classList.remove('listening');
    inputEl.placeholder = 'Message or use voice...';
    setStatus('Ready');
    if (inputEl.value.trim()) sendMessage();
  };

  recognition.onerror = (e) => {
    isListening = false;
    voiceBtn.classList.remove('listening');
    inputEl.placeholder = 'Message or use voice...';
    setStatus('Ready');
    if (e.error !== 'no-speech') console.warn('Speech error:', e.error);
  };
}

function toggleVoice() {
  if (!recognition) return;
  if (isListening) {
    recognition.stop();
  } else {
    recognition.start();
  }
}

// ── Service Worker ────────────────────────────────────────────────────────────

if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js').catch(() => {});
}

// ── Init ──────────────────────────────────────────────────────────────────────

setupVoice();
inputEl.focus();
