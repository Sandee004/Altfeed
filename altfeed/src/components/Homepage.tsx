import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { ArrowLeft, User, Users } from "lucide-react";

export default function HomePage() {
  interface Animal {
    name: string;
    icon: string;
  }

  const [animals, setAnimals] = useState<Animal[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const getAnimals = async () => {
      setLoading(true);
      setError(null);

      try {
        const response = await fetch("http://localhost:5000/api/animals");
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`); // More informative error
        }
        const data = await response.json();
        setAnimals(data);
      } catch (err) {
        // Type the error as unknown and narrow it down
        if (err instanceof Error) {
          setError(err.message || "Error fetching data."); // Display the error message or a default message
        } else {
          setError("An unknown error occurred.");
        }
        setError("Error fetching data."); // Display the error message or a default message
      } finally {
        setLoading(false);
      }
    };

    getAnimals();
  }, []);

  if (loading) return <p>Loading animals...</p>;

  if (error) return <p>{error}</p>;

  return (
    <div>
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
          <Link to="/profile">
            <User size={24} />
          </Link>
        </div>
      </nav>
      <h1 className="text-3xl font-bold px-10 my-6">Select an Animal</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 px-10">
        {animals.map((animal) => (
          <Link
            to={`/feeds/${animal.name.toLowerCase()}`}
            key={animal.name}
            className="block"
          >
            {" "}
            {/* Added block display */}
            <div className="hover:bg-gray-300 bg-gray-200 py-8 md:py-12 shadow-lg transition-shadow rounded-lg">
              {" "}
              {/* Added rounded corners */}
              <div>
                <p className="text-center text-3xl">{animal.icon}</p>
              </div>
              <div>
                <p className="text-center">{animal.name}</p>
              </div>
            </div>
          </Link>
        ))}
      </div>
      <div className="mt-8 text-center">
        <Link to="/submit-feed">
          <button className="bg-purple-900 hover:bg-purple-800 px-5 hover:shadow-lg py-3 rounded-md text-white">
            Submit a New Feed
          </button>
        </Link>
      </div>
    </div>
  );
}
