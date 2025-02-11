import { Link, useParams } from "react-router-dom";

const feedsData = {
  cattle: [
    { name: "Moringa Leaves", icon: "🍃" },
    { name: "Cassava Peels", icon: "🥔" },
    { name: "Brewers Grains", icon: "🍺" },
  ],
  poultry: [
    { name: "Black Soldier Fly Larvae", icon: "🐛" },
    { name: "Azolla", icon: "🌿" },
    { name: "Duckweed", icon: "🌱" },
  ],
  // Add more animals and their feeds here
};

export default function FeedsPage() {
  const { animal } = useParams<{ animal: string }>();

  if (!animal) return <p>Animal not found.</p>;

  const feeds = feedsData[animal.toLowerCase() as keyof typeof feedsData] || [];

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6 capitalize">{animal} Feeds</h1>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
        {feeds.length > 0 ? (
          feeds.map((feed) => (
            <Link
              to={`/feeds/${animal}/${feed.name
                .toLowerCase()
                .replace(/\s+/g, "-")}`}
              key={feed.name}
            >
              <div className="hover:shadow-lg transition-shadow">
                <div>
                  <p className="text-center">{feed.icon}</p>
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
    </div>
  );
}
