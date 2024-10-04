import Image from "next/image";
import ChatBox from "./components/ChatBot";

export default function Home() {
  return (
    <div className="h-screen bg-gray-50">
      <ChatBox />
    </div>
  );
}
