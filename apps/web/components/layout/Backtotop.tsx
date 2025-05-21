"use client";

import React from 'react';
import { useEffect } from 'react';
import { useState } from 'react';
import { ArrowUp } from 'lucide-react';

export default function BackToTop() {
    const [show, setShow] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            if (window.scrollY > 300) {
                setShow(true);
            } else {
                setShow(false);
            }
        };

        window.addEventListener('scroll', handleScroll);

        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    }, []);

    const scrollToTop = () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth',
        });
    };

    return (
        <>
            {show && (
                <button
                    onClick={scrollToTop}
                    className="fixed right-6 bottom-0 p-3 square-full bg-black dark:bg-gray-700 text-white shadow-lg hover:bg-gray-900 transition-colors z-50"
                    aria-label="Back to top"
                >
                    <ArrowUp className="w-6 h-12" />
                </button>
            )}
        </>
    );
}
