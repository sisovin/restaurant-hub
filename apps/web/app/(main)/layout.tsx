"use client"

import React from 'react';
import HeaderSection from '@/components/layout/HeaderSection';
import FooterSection from '@/components/layout/FooterSection';
// Define the MainLayout component

export default function MainLayout({
    children,
}: {
    children: React.ReactNode;
}) {  // Direct layout without animation wrappers
    return (
        <>
            <HeaderSection />
            <main>{children}</main>
            <FooterSection />
        </>
    )
}