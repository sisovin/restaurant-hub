'use client'

import Link from 'next/link'
import UserAvatar from './UserAvatar'
import ThemeSwitcher from './ThemeSwitcher'
import SocialGroups from './SocialGroups'
import { useEffect, useState } from 'react'
import { usePathname } from 'next/navigation'
import { Mail, Phone } from 'lucide-react'
import { Button } from '@/components/ui/button'
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
import { cn } from '@/lib/utils'

interface HeaderSectionProps {
    activeLink?: string;
}

export default function HeaderSection({ activeLink = 'home' }: HeaderSectionProps) {
    const pathname = usePathname()
    const [isSticky, setIsSticky] = useState(false)

    useEffect(() => {
        const handleScroll = () => setIsSticky(window.scrollY > 90)
        window.addEventListener('scroll', handleScroll)
        return () => window.removeEventListener('scroll', handleScroll)
    }, [])

    const navLink = (href: string, label: string) => {
        const isActive = pathname === href || (href === '/' && activeLink === 'home') ||
            (href.includes(activeLink) && activeLink !== 'home');
        return (
            <Link
                href={href}
                className={cn(
                    'text-sm font-semibold px-4 py-2 transition-colors hover:text-orange-500 font-body',
                    isActive && 'text-orange-500'
                )}
            >
                {label}
            </Link>
        );
    }

    return (
        <header className={cn('w-full z-50', isSticky && 'sticky top-0 bg-black shadow')}>
            <div className="grid grid-cols-[260px_1fr] grid-rows-2">
                {/* Left Logo (spans 2 rows) */}
                <div className="row-span-2 bg-orange-600 flex items-center justify-center">
                    <Link href="/" className="text-white text-3xl font-extrabold uppercase font-heading">
                        Chefer
                    </Link>
                </div>

                {/* Top Bar */}
                <div className="bg-[#1a1a1a] text-white text-sm px-6 py-2 flex justify-between items-center">
                    <div className="flex items-center gap-2">
                        <Mail size={16} className="text-orange-500" />
                        <span className="font-body">info@example.com</span>
                    </div>
                    <div className="flex items-center gap-2">
                        <Phone size={16} className="text-orange-500" />
                        <span className="font-body">+012 345 6789</span>
                    </div>
                </div>

                {/* Main Navigation and Socials */}
                <div className="bg-black text-white flex items-center justify-between px-6 py-3">
                    {/* Navigation */}
                    <nav className="flex items-center space-x-4">
                        {navLink('/', 'Home')}
                        {navLink('/about', 'About')}
                        {navLink('/menu', 'Menu')}
                        {navLink('/team', 'Chefs')}                        <DropdownMenu>
                            <DropdownMenuTrigger asChild>
                                <Button
                                    variant="ghost"
                                    className="text-sm font-semibold px-4 py-2 text-white hover:text-orange-500 font-body"
                                >
                                    Pages
                                </Button>
                            </DropdownMenuTrigger>
                            <DropdownMenuContent className="bg-neutral-900 text-white border-none rounded-md shadow-lg">
                                <DropdownMenuItem><Link href="/feature" className="font-body">Features</Link></DropdownMenuItem>
                                <DropdownMenuItem><Link href="/blog" className="font-body">Blog Post</Link></DropdownMenuItem>                                <DropdownMenuItem><Link href="/testimonial" className="font-body">Testimonial</Link></DropdownMenuItem>
                                <DropdownMenuItem><Link href="/404" className="font-body">404 Error</Link></DropdownMenuItem>
                            </DropdownMenuContent>
                        </DropdownMenu>
                        {navLink('/contact', 'Contact')}
                    </nav>

                    {/* Social Icons, Theme Switcher, and User Avatar */}
                    <div className="hidden lg:flex gap-3 items-center">
                        {/* User Avatar */}
                        <UserAvatar />
                        {/* Theme Switcher */}
                        <ThemeSwitcher />
                        {/* Social Groups */}
                        <SocialGroups />
                    </div>
                </div>
            </div>
        </header>
    )
}
