import { Link, useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { ArrowLeft, User, Users } from "lucide-react";

export default function FeedsPage() {
  interface Feed {
    name: string;
    icon: string;
  }

  const [feeds, setFeeds] = useState<Feed[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const { animal } = useParams<{ animal: string }>();

  useEffect(() => {
    const fetchFeeds = async () => {
      if (!animal) return;

      setLoading(true);
      setError(null);

      try {
        const response = await fetch(
          `http://localhost:5000/feeds/${animal.toLowerCase()}`
        );
        if (!response.ok) {
          throw new Error(`Error fetching feeds.`);
        }
        const data = await response.json();
        setFeeds(data);
      } catch {
        setError("Error fetching feeds.");
      } finally {
        setLoading(false);
      }
    };

    fetchFeeds();
  }, [animal]);

  if (loading)
    return (
      <div className="fixed inset-0 bg-black/40 flex justify-center items-center z-50">
        <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-white"></div>
      </div>
    );

  if (error) return <p>{error}</p>;

  return (
    <>
      <nav className="bg-purple-900 flex justify-between items-center text-white p-4 fixed top-0 left-0 right-0 z-50">
        <Link to="/homepage" className="flex items-center">
          <ArrowLeft className="mr-2" />
          Back
        </Link>
        <Link to="/" className="text-2xl font-bold">
          AltFeed
        </Link>
        <div className="flex items-center space-x-4">
          <Link to="/community">
            <Users size={24} />
          </Link>
          <Link to="/profile">
            <User size={24} />
          </Link>
        </div>
      </nav>

      <div className="pt-16 md:pt-20">
        <h1 className="text-3xl font-bold px-10 my-6 capitalize">
          {animal} Feeds
        </h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 px-10">
          {feeds.length > 0 ? (
            feeds.map((feed) => (
              <Link
                to={
                  animal
                    ? `/feed/${animal.toLowerCase()}/${feed.name
                        .toLowerCase()
                        .replace(/\s+/g, "-")}`
                    : "#"
                }
                key={feed.name}
                className="block"
              >
                <div className="hover:bg-gray-300 bg-gray-200 py-8 md:py-12 shadow-lg transition-shadow rounded-lg">
                  <div>
                    <p className="text-center text-3xl">🌿</p>
                  </div>
                  <div>
                    <p className="text-center">{feed.name}</p>
                  </div>
                </div>
              </Link>
            ))
          ) : (
            <p>No feeds available for {animal}.</p>
          )}
        </div>
        <div className="mt-8 text-center">
          <Link to="/submit-feed">
            <button className="bg-purple-900 hover:bg-purple-800 px-5 hover:shadow-lg py-3 rounded-md text-white">
              Submit a New Feed
            </button>
          </Link>
        </div>
      </div>
    </>
  );
}
