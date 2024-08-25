export default function Navbar() {
  return (
    <nav className="flex items-center justify-between w-full h-16 px-8 bg-gray-100">
      <h1 className="text-2xl font-bold">Logo</h1>
      <ul className="flex items-center gap-4">
        <li>
          <a href="#">Home</a>
        </li>
        <li>
          <a href="#">About</a>
        </li>
        <li>
          <a href="#">Services</a>
        </li>
        <li>
          <a href="#">Contact</a>
        </li>
      </ul>
    </nav>
  );
}
