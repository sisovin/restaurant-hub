
"use client";
import * as React from "react";
import { User, LogOut, Settings, UserCircle } from "lucide-react";
import {
    DropdownMenu,
    DropdownMenuTrigger,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuSeparator,
} from "@/components/ui/dropdown-menu";

export default function UserAvatar() {
    return (
        <DropdownMenu>
            <DropdownMenuTrigger asChild>
                <button
                    className="flex items-center justify-center rounded-full bg-muted w-9 h-9 focus:outline-none"
                    aria-label="User menu"
                >
                    <UserCircle className="size-6 text-muted-foreground" />
                </button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end" className="w-48 bg-white text-gray-900 dark:bg-neutral-900 dark:text-white border border-gray-200 dark:border-neutral-800 shadow-lg">
                <DropdownMenuItem>
                    <User className="size-4 mr-2" /> Profile
                </DropdownMenuItem>
                <DropdownMenuItem>
                    <Settings className="size-4 mr-2" /> Settings
                </DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem variant="destructive">
                    <LogOut className="size-4 mr-2" /> Logout
                </DropdownMenuItem>
            </DropdownMenuContent>
        </DropdownMenu>
    );
}
