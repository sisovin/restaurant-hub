"use client";
import Link from "next/link";
import { cn } from "@/lib/utils";
import { Facebook, Twitter, Linkedin, Mail, Phone, Instagram } from "lucide-react";
import { LucideIcon } from "lucide-react";

// Define the available icon names as a type
type SocialIconName = 'facebook' | 'twitter' | 'linkedin' | 'instagram' | 'mail' | 'phone';

// Map of social media icons using Lucide React components
const SOCIAL_ICONS: Record<SocialIconName, LucideIcon> = {
    facebook: Facebook,
    twitter: Twitter,
    linkedin: Linkedin,
    instagram: Instagram,
    mail: Mail,
    phone: Phone,
};

// Define the social link type
interface SocialLink {
    icon: SocialIconName;
    label: string;
    href: string;
}

const SOCIALS: SocialLink[] = [
    { icon: "facebook", label: "Facebook", href: "#" },
    { icon: "twitter", label: "Twitter", href: "#" },
    { icon: "linkedin", label: "LinkedIn", href: "#" },
];

export default function SocialGroups() {
    return (
        <div className="flex gap-3 items-center">
            {SOCIALS.map(({ icon, label, href }) => {
                const IconComponent = SOCIAL_ICONS[icon];
                return (
                    <Link
                        key={icon}
                        href={href}
                        className={cn(
                            "group w-9 h-9 flex items-center justify-center border rounded-full transition",
                            "border-gray-300 dark:border-gray-400",
                            "text-gray-500 dark:text-gray-400",
                            "bg-gray-200 dark:bg-black",
                            "hover:bg-orange-500 dark:hover:bg-gray-200" 
                        )}
                        aria-label={`${label} social link`}
                    >
                        <IconComponent
                            className={cn(
                                "w-4 h-4",
                                "transition",
                                "text-orange-500", // Base color for light mode
                                "dark:text-orange-400", // Override for dark mode
                                "group-hover:text-white"
                            )}
                        />
                    </Link>
                );
            })}
        </div>
    );
}
