import { Link, useLocation } from "react-router-dom";
import { ArrowLeft, User, Users } from "lucide-react";

export default function Navbar() {
  const { pathname } = useLocation();

  return (
    <nav className="bg-purple-900 text-white p-4">
      <div className="container mx-auto flex justify-between items-center">
        {pathname !== "/" && (
          <Link to="/" className="flex items-center">
            <ArrowLeft className="mr-2" />
            Back
          </Link>
        )}
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
      </div>
    </nav>
  );
}
