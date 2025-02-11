"use client";

import { useState } from "react";
import { Search } from "lucide-react";

export default function SearchFeeds({
  onSearch,
}: {
  onSearch: (query: string) => void;
}) {
  const [query, setQuery] = useState("");

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    onSearch(query);
  };

  return (
    <form onSubmit={handleSearch} className="flex gap-2 mb-4">
      <input
        type="text"
        placeholder="Search feeds..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="flex-grow"
      />
      <button type="submit" className="bg-purple-700 hover:bg-purple-800">
        <Search className="mr-2" />
        Search
      </button>
    </form>
  );
}
