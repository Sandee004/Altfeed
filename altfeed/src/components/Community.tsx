import { useNavigate } from "react-router-dom";

const Community = () => {
  const navigate = useNavigate();
  const handleBackClick = () => {
    navigate(-1);
  };
  return (
    <div className="fixed inset-0 bg-black/50 flex justify-center items-center z-50">
      <div className="bg-white p-8 rounded-lg shadow-lg text-center">
        <h2 className="text-3xl font-bold text-purple-900 mb-4">Coming Soon</h2>
        <p className="text-lg text-gray-700">
          We're working on something great. Stay tuned!
        </p>
        <button
          onClick={handleBackClick}
          className="bg-purple-900 text-white px-6 py-3 rounded-md hover:bg-purple-800 transition"
        >
          Go Back
        </button>
      </div>
    </div>
  );
};

export default Community;
