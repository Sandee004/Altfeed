import { useParams } from "react-router-dom";

const feedDetails: Record<string, { name: string; description: string; instructions: string[] }> = {
  "moringa-leaves": {
    name: "Moringa Leaves",
    description:
      "Moringa leaves are highly nutritious and can be used as a protein supplement for livestock.",
    instructions: [
      "Harvest fresh moringa leaves",
      "Dry the leaves in a shaded area for 3-4 days",
      "Grind the dried leaves into a powder",
      "Mix 10-20% of moringa leaf powder with regular feed",
    ],
  },
  "cassava-peels": {
    name: "Cassava Peels",
    description:
      "Cassava peels are a good energy source for livestock and should be properly processed before feeding.",
    instructions: [
      "Collect fresh cassava peels",
      "Sun-dry them for 3-5 days",
      "Chop or grind into smaller pieces",
      "Mix with other feed components",
    ],
  },
  // Add more feed details here
};

export default function FeedDetail() {
  const { feedname } = useParams<{ feedname: string }>();

  if (!feedname) {
    return <div className="text-red-500">Feed not specified.</div>;
  }

  const feed = feedDetails[feedname.toLowerCase()];

  if (!feed) {
    return <div className="text-red-500">Feed not found.</div>;
  }

  return (
    <div>
      <h1 className="text-3xl font-bold mb-4">{feed.name}</h1>
      <p className="mb-4">{feed.description}</p>
      <h2 className="text-xl font-semibold mb-2">Instructions:</h2>
      <ol className="list-decimal list-inside">
        {feed.instructions.map((instruction, index) => (
          <li key={index}>{instruction}</li>
        ))}
      </ol>
    </div>
  );
}
