import { ArrowLeft, Play, Users } from "lucide-react";
import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";

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
  const navigate = useNavigate();

  useEffect(() => {
    const fetchFeedDetails = async () => {
      if (!animal || !feedname) return;

      setLoading(true);
      setError(null);

      try {
        const response = await fetch(
          `https://altfeed-backend.onrender.com/api/feeds/${animal.toLowerCase()}/${feedname.toLowerCase()}`
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

  if (loading)
    return (
      <div className="fixed inset-0 bg-black/40 flex justify-center items-center z-50">
        <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-white"></div>
      </div>
    );

  if (error) return <p>{error}</p>;

  if (!feed) return <p>No feed details available.</p>;

  const handleBackClick = () => {
    navigate(`/feeds/${animal}`);
  };

  const watchVideo = () => {
    alert("Coming soon.....");
  };
  return (
    <>
      <nav className="bg-purple-900 flex justify-between items-center text-white p-4 fixed top-0 left-0 right-0 z-50">
        <div onClick={handleBackClick} className="flex items-center">
          <ArrowLeft className="mr-2" />
          Back
        </div>
        <Link to="/" className="text-2xl font-bold">
          AltFeed
        </Link>
        <div className="flex items-center space-x-4">
          <Link to="/community">
            <Users size={24} />
          </Link>
        </div>
      </nav>
      <div className="px-6 pb-6 pt-20 md:pt-25">
        <h1 className="text-3xl font-bold mb-4">{feed.feed_name}</h1>
        <h2 className="text-xl font-semibold mb-4">Instructions:</h2>
        <ol className="list-decimal list-inside">
          {feed.preparation.map((preparation, index) => (
            <li key={index} className="text-md text-gray-700">
              {preparation}
            </li>
          ))}
        </ol>

        <button
          onClick={watchVideo}
          className="bg-purple-900 text-white flex gap-2 hover:cursor-pointer hover:bg-purple-800 justify-center items-center px-4 py-2 mt-4 rounded-md"
        >
          See video <Play size={17} />
        </button>
      </div>
    </>
  );
}
