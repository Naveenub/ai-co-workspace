import React from "react";
import WorkspaceSidebar from "./components/WorkspaceSidebar";

function App() {
  return (
    <div className="flex h-screen bg-gray-100">
      <WorkspaceSidebar />
      <div className="flex-1 p-6">
        <h1 className="text-2xl font-bold">AI Co-Workspace</h1>
        <p>Welcome! Select a workspace to start collaborating.</p>
      </div>
    </div>
  );
}

export default App;
