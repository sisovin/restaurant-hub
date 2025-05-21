
{/* Back to Top */ }
import React from 'react';
import { useEffect } from 'react';
import { useState } from 'react';

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
                <a href="#" className="btn btn-dark py-3 fs-4 back-to-top" aria-label="Back to top" onClick={scrollToTop}><i className="bi bi-arrow-up"></i></a>
            )}
        </>
    );
}
