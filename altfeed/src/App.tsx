import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./components/Homepage";
import IntroPage from "./components/Intro";
import FeedsPage from "./components/FeedsPage";
import FeedDetails from "./components/FeedDetails";
import ProfilePage from "./components/Profile";
import Community from "./components/Community";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<IntroPage />} />
        <Route path="/homepage" element={<HomePage />} />
        <Route path="/feeds/:animal" element={<FeedsPage />} />
        <Route path="/feed/:animal/:feedname" element={<FeedDetails />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/community" element={<Community />} />
      </Routes>
    </Router>
  );
}

export default App;
