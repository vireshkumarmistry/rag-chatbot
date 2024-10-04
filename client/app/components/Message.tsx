import { marked } from "marked";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faRobot, faUser } from '@fortawesome/free-solid-svg-icons';

interface MessageProps {
  message: {
    id: number;
    text: string;
    sender: 'user' | 'bot';
    isHtml?: boolean;
  };
}

const Message = ({ message }: MessageProps) => {
  const formattedText = marked(message.text);

  return (
    <div className={`p-2 ${message.sender === 'user' ? 'text-right' : 'text-left'}`}>
      <div className={`flex items-center ${message.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
        {message.sender === 'bot' && (
          <FontAwesomeIcon icon={faRobot} className="mr-2 text-gray-200" />
        )}
        {message.sender === 'user' && (
          <FontAwesomeIcon icon={faUser} className="mr-2 text-blue-500" />
        )}
        <div
          className={`inline-block px-4 py-2 rounded ${
            message.sender === 'user' ? 'bg-blue-500 text-white' : 'bg-gray-200 text-black'
          }`}
        >
          {message.isHtml ? (
            <div dangerouslySetInnerHTML={{ __html: formattedText }} />
          ) : (
            message.text
          )}
        </div>
      </div>
    </div>
  );
};

export default Message;
