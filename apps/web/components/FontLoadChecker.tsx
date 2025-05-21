'use client';
import { useEffect, useState } from 'react';

export default function FontLoadChecker() {
    const [fontsStatus, setFontsStatus] = useState({
        emblemaOne: false,
        poppinsRegular: false,
        poppinsMedium: false,
        poppinsSemiBold: false
    });
    const [visible, setVisible] = useState(true);

    useEffect(() => {
        // Check if custom fonts are loaded
        document.fonts.ready.then(() => {
            const emblemaLoaded = document.fonts.check('1em "Emblema One"');
            const poppinsRegularLoaded = document.fonts.check('400 1em "Poppins"');
            const poppinsMediumLoaded = document.fonts.check('500 1em "Poppins"');
            const poppinsSemiBoldLoaded = document.fonts.check('600 1em "Poppins"');

            console.log('Emblema One font loaded:', emblemaLoaded);
            console.log('Poppins Regular font loaded:', poppinsRegularLoaded);
            console.log('Poppins Medium font loaded:', poppinsMediumLoaded);
            console.log('Poppins SemiBold font loaded:', poppinsSemiBoldLoaded);

            setFontsStatus({
                emblemaOne: emblemaLoaded,
                poppinsRegular: poppinsRegularLoaded,
                poppinsMedium: poppinsMediumLoaded,
                poppinsSemiBold: poppinsSemiBoldLoaded
            });

            // Hide the indicator after 10 seconds
            setTimeout(() => setVisible(false), 10000);
        });
    }, []);    if (!visible) return null;
    return (
        <div 
            style={{
                position: 'fixed',
                bottom: '10px',
                right: '10px',
                background: '#333',
                color: '#fff',
                padding: '8px 12px',
                borderRadius: '4px',
                zIndex: 9999,
                fontFamily: 'system-ui',
                fontSize: '12px',
                opacity: 0.8,
                maxWidth: '250px',
                cursor: 'pointer',
            }}
            onClick={() => setVisible(false)}
        >
            <div>Fonts loaded:</div>
            <div>- Emblema One: {fontsStatus.emblemaOne ? '✓' : '✗'}</div>
            <div>- Poppins Regular: {fontsStatus.poppinsRegular ? '✓' : '✗'}</div>
            <div>- Poppins Medium: {fontsStatus.poppinsMedium ? '✓' : '✗'}</div>
            <div>- Poppins SemiBold: {fontsStatus.poppinsSemiBold ? '✓' : '✗'}</div>
            <div style={{ fontSize: '10px', marginTop: '4px' }}>Click to dismiss</div>
        </div>
    );
}