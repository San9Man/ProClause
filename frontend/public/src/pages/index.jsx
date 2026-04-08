import { useState } from "react";
const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

const renderAIResponse = (data) => {
    if (!data) return null;

    const color =
        data.risk_level === "HIGH"
            ? "bg-red-600"
            : data.risk_level === "MEDIUM"
                ? "bg-yellow-500"
                : "bg-green-600";

    return (
        <div className="space-y-3">
            <div className={`inline-block px-3 py-1 rounded ${color}`}>
                {data.risk_level} RISK
            </div>

            <div>
                <h3 className="font-semibold">📄 Explanation</h3>
                <p>{data.explanation}</p>
            </div>

            {data.obligations?.length > 0 && (
                <div>
                    <h3 className="font-semibold">💰 Obligations</h3>
                    <ul className="list-disc ml-5">
                        {data.obligations.map((o, i) => (
                            <li key={i}>{o}</li>
                        ))}
                    </ul>
                </div>
            )}

            <div>
                <h3 className="font-semibold">💡 Recommendation</h3>
                <p>{data.recommendation}</p>
            </div>
        </div>
    );
};
export default function App() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");
    const [file, setFile] = useState(null);
    const [persona, setPersona] = useState("Tenant");

    const sendMessage = async () => {
        if (!input) return;

        const newMessages = [...messages, { role: "user", text: input }];
        setMessages(newMessages);

        const res = await fetch(`${API_URL}/ask`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                query: input,
                persona: persona,
            }),
        });

        const data = await res.json();

        setMessages([
            ...newMessages,
            {
                role: "ai",
                data,
            },
        ]);

        setInput("");
    };

    const uploadFile = async () => {
        if (!file) return;

        const formData = new FormData();
        formData.append("file", file);

        await fetch(`${API_URL}/upload`, {
            method: "POST",
            body: formData,
        });

        alert("✅ Document processed!");
    };

    return (
        <div className="h-screen flex flex-col bg-gray-900 text-white">

            {/* HEADER */}
            <div className="p-4 text-xl font-bold border-b border-gray-700">
                ⚖️ Legal AI Agent
            </div>

            {/* TOP BAR */}
            <div className="p-3 flex gap-3 border-b border-gray-700">

                <input
                    type="file"
                    onChange={(e) => setFile(e.target.files[0])}
                />

                <button
                    onClick={uploadFile}
                    className="bg-green-600 px-4 py-2 rounded"
                >
                    Upload
                </button>

                <select
                    value={persona}
                    onChange={(e) => setPersona(e.target.value)}
                    className="bg-gray-800 px-3 py-2 rounded"
                >
                    <option>Tenant</option>
                    <option>Landlord</option>
                    <option>Employee</option>
                    <option>Employer</option>
                    <option>Buyer</option>
                </select>
            </div>

            {/* CHAT */}
            <div className="flex-1 overflow-y-auto p-4 space-y-4">
                {messages.map((msg, i) => (
                    <div key={i} className="max-w-xl">
                        {msg.role === "user" ? (
                            <div className="bg-blue-600 p-3 rounded-lg ml-auto">
                                {msg.text}
                            </div>
                        ) : (
                            <div className="bg-gray-700 p-3 rounded-lg">
                                {renderAIResponse(msg.data)}
                            </div>
                        )}
                    </div>
                ))}
            </div>

            {/* INPUT */}
            <div className="p-4 border-t border-gray-700 flex gap-2">
                <input
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    className="flex-1 p-2 rounded bg-gray-800"
                    placeholder="Ask about your legal document..."
                />

                <button
                    onClick={sendMessage}
                    className="bg-blue-600 px-5 rounded"
                >
                    Send
                </button>
            </div>
        </div>
    );
}