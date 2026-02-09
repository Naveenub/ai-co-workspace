import React, { useState } from "react";

const ArtifactEditor = () => {
  const [content, setContent] = useState("");

  return (
    <div className="p-4 bg-white shadow rounded">
      <textarea
        className="w-full h-32 p-2 border border-gray-300 rounded"
        placeholder="Write artifact content..."
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />
    </div>
  );
};

export default ArtifactEditor;
