import React from "react";

interface MarkdownViewerProps {
  content: string;
}

const MarkdownViewer: React.FC<MarkdownViewerProps> = ({ content }) => {
  return (
    <div className="p-4 bg-gray-50 border border-gray-200 rounded">
      {content ? <pre>{content}</pre> : "No content to display"}
    </div>
  );
};

export default MarkdownViewer;
