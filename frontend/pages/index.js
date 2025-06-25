
import { useState, useEffect, useRef } from 'react';
import axios from 'axios';

export default function Home() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const ws = useRef(null);

  useEffect(() => {
    ws.current = new WebSocket('ws://localhost:8000/ws');
    ws.current.onmessage = (e) => {
      const data = JSON.parse(e.data);
      setMessages((prev) => [...prev, data]);
    };
  }, []);

  const sendMsg = () => {
    ws.current.send(JSON.stringify({ content: input }));
    setMessages((prev) => [...prev, { role: 'user', content: input }]);
    setInput('');
  };

  return (
    <main className="min-h-screen flex flex-col items-center p-4">
      <h1 className="text-3xl font-bold mb-4">Jester AI - TS</h1>
      <div className="w-full max-w-3xl border rounded shadow p-4 flex flex-col gap-2 h-[60vh] overflow-y-auto">
        {messages.map((m, i) => (
          <div key={i} className={m.role === 'assistant' ? 'text-blue-700' : 'text-black'}>
            <strong>{m.role === 'assistant' ? 'Jester' : 'You'}:</strong> {m.content}
          </div>
        ))}
      </div>
      <div className="mt-4 w-full max-w-3xl flex gap-2">
        <input value={input} onChange={(e)=>setInput(e.target.value)}
               className="flex-1 border p-2 rounded" placeholder="Type message..." />
        <button onClick={sendMsg} className="bg-blue-600 text-white px-4 rounded">Send</button>
      </div>
    </main>
  );
}
