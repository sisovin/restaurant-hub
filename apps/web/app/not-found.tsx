"use client"

import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { HomeIcon, ChevronRightIcon, SearchIcon } from 'lucide-react';
import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function NotFound() {
  const [searchQuery, setSearchQuery] = useState('');
  const router = useRouter();

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      router.push(`/search?q=${encodeURIComponent(searchQuery)}`);
    }
  };

  return (
    <div className="container flex flex-col items-center justify-center max-w-md min-h-[70vh] mx-auto py-16 text-center">
      <h1 className="text-9xl font-bold text-primary">404</h1>
      <h2 className="mt-4 text-3xl font-bold">Page Not Found</h2>

      <p className="mt-6 text-muted-foreground">
        The page you are looking for doesn&apos;t exist or has been moved.
      </p>

      <form onSubmit={handleSearch} className="flex w-full mt-8 gap-2">
        <div className="relative flex-grow">
          <SearchIcon className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search our site..."
            className="w-full pl-10 py-2 pr-4 border border-input rounded-md bg-background focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary"
          />
        </div>
        <Button type="submit">Search</Button>
      </form>

      <div className="flex items-center gap-2 mt-8">
        <Link href="/">
          <Button variant="outline" size="sm">
            <HomeIcon className="mr-2 h-4 w-4" />
            Home
          </Button>
        </Link>
        <ChevronRightIcon className="h-4 w-4 text-muted-foreground" />
        <Link href="/destination">
          <Button variant="outline" size="sm">Destinations</Button>
        </Link>
        <ChevronRightIcon className="h-4 w-4 text-muted-foreground" />
        <Link href="/contact">
          <Button variant="outline" size="sm">Contact</Button>
        </Link>
      </div>

      <p className="mt-12 text-sm text-muted-foreground">
        If you believe this is an error, please <Link href="/contact" className="text-primary hover:underline">contact our support team</Link>.
      </p>
    </div>
  );
}
