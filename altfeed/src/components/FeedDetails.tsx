import { ArrowLeft, Users } from "lucide-react";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

interface FeedDetails {
  name: string;
  feed_name: string;
  preparation: string[];
}

export default function FeedDetail() {
  const { animal, feedname } = useParams<{
    animal: string;
    feedname: string;
  }>();
  const [feed, setFeed] = useState<FeedDetails | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchFeedDetails = async () => {
      if (!animal || !feedname) return;

      setLoading(true);
      setError(null);

      try {
        const response = await fetch(
          `http://localhost:5000/api/feeds/${animal.toLowerCase()}/${feedname.toLowerCase()}`
        );
        if (!response.ok) {
          throw new Error(`Feed not found!`);
        }
        const data = await response.json();
        setFeed(data);
      } catch (err) {
        console.error("Error fetching feed details:", err);
        setError(
          err instanceof Error ? err.message : "Error fetching feed details."
        );
      } finally {
        setLoading(false);
      }
    };

    fetchFeedDetails();
  }, [animal, feedname]);

  if (loading) return <p>Loading feed details...</p>;

  if (error) return <p>{error}</p>;

  if (!feed) return <p>No feed details available.</p>;

  return (
    <>
      <nav className="bg-purple-900 flex justify-between items-center text-white p-4">
        <Link to="/" className="flex items-center">
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
        </div>
      </nav>
      <div className="px-6 py-6">
        <h1 className="text-3xl font-bold mb-4">{feed.feed_name}</h1>
        <h2 className="text-xl font-semibold mb-4">Instructions:</h2>
        <ol className="list-decimal list-inside">
          {feed.preparation.map((preparation, index) => (
            <li key={index} className="text-md text-gray-700">
              {preparation}
            </li>
          ))}
        </ol>
      </div>
    </>
  );
}
