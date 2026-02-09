import React from "react";

const WorkspaceSidebar = () => {
  return (
    <div className="w-64 bg-white shadow-md p-4">
      <h2 className="font-bold mb-4">Workspaces</h2>
      <ul>
        <li className="py-1 hover:bg-gray-200 cursor-pointer">Workspace 1</li>
        <li className="py-1 hover:bg-gray-200 cursor-pointer">Workspace 2</li>
      </ul>
    </div>
  );
};

export default WorkspaceSidebar;
