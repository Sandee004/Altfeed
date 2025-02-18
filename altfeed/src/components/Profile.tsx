import { ArrowLeft } from "lucide-react";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

interface UserData {
  name: string;
  email: string;
  farm_type: string;
  location: string;
  size: string;
  phone: string;
  profile_image_url: string;
}

export default function ProfilePage() {
  const [userData, setUserData] = useState<UserData | null>(null);
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    farm_type: "",
    location: "",
    size: "",
    phone: "",
    profile_image_url: "",
  });

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const response = await fetch("http://localhost:5000/profile");
        if (response.ok) {
          const data = await response.json();
          setUserData(data);
        } else if (response.status === 404) {
          setUserData(null);
        }
      } catch (error) {
        console.error("Error fetching user data:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchUserData();
  }, []);

  // Open modal and set form data
  const handleButtonClick = () => {
    if (userData) {
      setFormData(userData); // Prefill form for updating profile
    } else {
      setFormData({
        // Empty form for creating account
        name: "",
        email: "",
        farm_type: "",
        location: "",
        size: "",
        phone: "",
        profile_image_url: "",
      });
    }
    setShowModal(true);
  };

  // Handle form input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  // Close modal
  const closeModal = () => {
    setShowModal(false);
  };

  // Handle form submission
  const handleSubmit = async (
    e: React.FormEvent<HTMLFormElement>
  ): Promise<void> => {
    e.preventDefault();
    try {
      const url: string = userData
        ? "http://localhost:5000/update_user"
        : "http://localhost:5000/create_user";
      const method: string = userData ? "PUT" : "POST";
      const response: Response = await fetch(url, {
        method: method,
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        alert("Profile saved successfully!");
        setShowModal(false);
        // Refresh profile data
        const updatedData: Response = await fetch(
          "http://localhost:5000/profile"
        );
        const newData: UserData = await updatedData.json();
        setUserData(newData);
      } else {
        alert("Failed to save profile.");
      }
    } catch (error) {
      console.error("Error saving profile:", error);
      alert("An error occurred. Please try again.");
    }
  };

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <>
      <nav className="bg-purple-900 flex justify-between items-center text-white p-4 fixed top-0 left-0 right-0 z-50">
        <Link to="/homepage" className="w-1/3 flex items-center">
          <ArrowLeft className="mr-2" />
          Back
        </Link>
        <Link to="/" className="text-2xl text-center font-bold w-1/3">
          AltFeed
        </Link>
        <div className="w-1/3"></div>
      </nav>
      <div className="bg-gray-100 min-h-screen pt-16">
        <div className="container mx-auto p-8">
          <div className="bg-white rounded-lg shadow-lg p-8">
            <div className="flex justify-center mb-6">
              <div className="rounded-full h-32 w-32 bg-gray-300 flex items-center justify-center overflow-hidden">
                <img
                  src={
                    userData?.profile_image_url ||
                    "https://via.placeholder.com/128"
                  }
                  alt="Profile"
                  className="object-cover h-full w-full"
                />
              </div>
            </div>
            <div className="text-center mb-6">
              <h2 className="text-2xl font-bold mb-2">
                {userData?.name || "Guest"}
              </h2>
              <p className="text-gray-700">
                {userData?.email || "No Email Provided"}
              </p>
              <p className="text-gray-700">
                Farm Type: {userData?.farm_type || "N/A"}
              </p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <h3 className="text-lg font-semibold mb-2">Farm Details</h3>
                <p>Location: {userData?.location || "N/A"}</p>
                <p>Size: {userData?.size || "N/A"}</p>
              </div>
              <div>
                <h3 className="text-lg font-semibold mb-2">Contact</h3>
                <p>Phone: {userData?.phone || "N/A"}</p>
              </div>
            </div>
            <div className="mt-6 text-center">
              <button
                onClick={handleButtonClick}
                className="bg-purple-900 hover:bg-purple-800 text-white font-bold py-2 px-4 rounded"
              >
                {userData ? "Update Profile" : "Create Account"}
              </button>
            </div>
          </div>
        </div>

        {/* Modal */}
        {showModal && (
          <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
            <div className="bg-white rounded-lg w-11/12 md:w-1/2 p-8 relative">
              <h2 className="text-2xl font-bold mb-4">
                {userData ? "Update Profile" : "Create Account"}
              </h2>
              <form onSubmit={handleSubmit}>
                <input
                  type="text"
                  name="name"
                  placeholder="Name"
                  value={formData.name}
                  onChange={handleChange}
                  className="w-full mb-4 p-2 border rounded"
                />
                <input
                  type="email"
                  name="email"
                  placeholder="Email"
                  value={formData.email}
                  onChange={handleChange}
                  className="w-full mb-4 p-2 border rounded"
                />
                <input
                  type="text"
                  name="farm_type"
                  placeholder="Farm Type"
                  value={formData.farm_type}
                  onChange={handleChange}
                  className="w-full mb-4 p-2 border rounded"
                />
                <input
                  type="text"
                  name="location"
                  placeholder="Location"
                  value={formData.location}
                  onChange={handleChange}
                  className="w-full mb-4 p-2 border rounded"
                />
                <input
                  type="text"
                  name="size"
                  placeholder="Farm Size"
                  value={formData.size}
                  onChange={handleChange}
                  className="w-full mb-4 p-2 border rounded"
                />
                <input
                  type="text"
                  name="phone"
                  placeholder="Phone"
                  value={formData.phone}
                  onChange={handleChange}
                  className="w-full mb-4 p-2 border rounded"
                />
                <input
                  type="text"
                  name="profile_image_url"
                  placeholder="Profile Image URL"
                  value={formData.profile_image_url}
                  onChange={handleChange}
                  className="w-full mb-4 p-2 border rounded"
                />
                <div className="flex justify-end space-x-4">
                  <button
                    type="button"
                    onClick={closeModal}
                    className="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded"
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    className="bg-purple-900 hover:bg-purple-800 text-white font-bold py-2 px-4 rounded"
                  >
                    Save
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}
      </div>
    </>
  );
}
