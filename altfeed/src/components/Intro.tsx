import { Link } from "react-router-dom";
import Navbar from "./Navbar";

export default function IntroPage() {
  return (
    <>
      <Navbar />
      <div
        className="relative bg-cover bg-center h-screen flex items-center justify-center text-white"
        style={{ backgroundImage: "url('/images/hero-bg.jpg')" }}
      >
        <div className="bg-black bg-opacity-50 p-8 text-center rounded-lg">
          <h1 className="text-5xl font-bold mb-4">Welcome to AltFeed</h1>
          <p className="text-xl mb-6 max-w-2xl">
            Providing innovative and sustainable alternative feed options for
            your livestock.
          </p>
          <Link to="/homepage">
            <button className="bg-purple-900 hover:bg-purple-700 text-white py-3 px-6 text-lg rounded-lg transition">
              Get Started
            </button>
          </Link>
        </div>
      </div>

      {/* Features Section */}
      <section className="py-16 px-8 bg-gray-100 text-gray-900">
        <h2 className="text-3xl font-bold text-center mb-10">
          Why Choose AltFeed?
        </h2>
        <div className="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">
          <div className="bg-white p-6 rounded-lg shadow-md text-center">
            <img
              src="/images/sustainable.svg"
              alt="Sustainable"
              className="mx-auto mb-4 w-20"
            />
            <h3 className="text-2xl font-semibold mb-2">
              Sustainable Solutions
            </h3>
            <p>
              Reduce feed costs with locally available, non-conventional feed
              sources.
            </p>
          </div>

          <div className="bg-white p-6 rounded-lg shadow-md text-center">
            <img
              src="/images/nutrition.svg"
              alt="Nutrition"
              className="mx-auto mb-4 w-20"
            />
            <h3 className="text-2xl font-semibold mb-2">Optimized Nutrition</h3>
            <p>
              Discover feeds rich in proteins, vitamins, and minerals to improve
              livestock health.
            </p>
          </div>

          <div className="bg-white p-6 rounded-lg shadow-md text-center">
            <img
              src="/images/community.svg"
              alt="Community"
              className="mx-auto mb-4 w-20"
            />
            <h3 className="text-2xl font-semibold mb-2">Farmer-Friendly</h3>
            <p>
              Easy-to-follow guides and step-by-step instructions tailored for
              all farmers.
            </p>
          </div>
        </div>
      </section>

      {/* Call-to-Action */}
      <div className="text-center py-16 bg-purple-900 text-white">
        <h2 className="text-3xl font-bold mb-4">
          Start Exploring Alternative Feeds Today!
        </h2>
        <Link to="/homepage">
          <button className="bg-white text-purple-900 hover:bg-gray-200 py-3 px-6 text-lg rounded-lg transition">
            Explore Feeds
          </button>
        </Link>
      </div>
    </>
  );
}
