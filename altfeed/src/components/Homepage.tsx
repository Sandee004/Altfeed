import { Link } from "react-router-dom";
import Navbar from "./Navbar";
const animals = [
  { name: "Cattle", icon: "🐄" },
  { name: "Poultry", icon: "🐔" },
  { name: "Pigs", icon: "🐖" },
  { name: "Sheep", icon: "🐑" },
  { name: "Goats", icon: "🐐" },
];

export default function HomePage() {
  return (
    <div>
      <Navbar />
      <h1 className="text-3xl font-bold px-6 my-6">Select an Animal</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 px-8">
        {animals.map((animal) => (
          <Link to={`/feeds/${animal.name.toLowerCase()}`} key={animal.name}>
            <div className="hover:bg-gray-200 bg-gray-100 py-8 md:py-12 hover:shadow-lg transition-shadow">
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
