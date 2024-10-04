import Image from "next/image";
import ChatBox from "./components/ChatBot";

export default function Home() {
  return (
    <div className="h-screen">
      <ChatBox />
    </div>
  );
}
