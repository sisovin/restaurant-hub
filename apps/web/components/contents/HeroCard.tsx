'use client';
import React from 'react';
import Image from 'next/image';
import styles from './HeroCard.module.css'; // Assuming you have a CSS module for styles
const HeroCard = () => {
    return (
        <div className="container-fluid p-5 mb-5 bg-dark text-secondary">
            {/* Hero Start */}

            {/* Centered Heading */}            <div className="w-100 d-flex justify-content-center mb-5">
                <h1 className="display-1 text-secondary mb-0 font-heading">John Doe</h1>
            </div>

            {/* Grid layout for images and text */}
            <div className="row g-5 py-5">
                <div className="col-lg-4">
                    <div className="position-relative mb-3">
                        <Image
                            className="img-fluid rounded"
                            src="/images/hero-2.jpg"
                            alt="Hero"
                            width={600}
                            height={400}
                            style={{ objectFit: "cover" }}
                        />
                    </div>                    <p>
                        <i className={`bi bi-arrow-down animate-up-down ${styles.arrowIcon}`}></i>
                    </p>
                    <p className="mb-0 font-body">
                        Diam dolor diam ipsum et, tempor voluptua sit consetetur sit. Aliquyam diam amet diam et eos sadipscing labore. Clita erat ipsum et lorem et sit, sed stet no labore lorem sit. Sanctus clita duo justo et tempor consetetur takimata eirmod.
                    </p>
                </div>

                <div className={`col-lg-4 ${styles.heroMinHeight}`}>
                    <div className="position-relative h-100">
                        <Image
                            className="position-absolute w-100 h-100 rounded"
                            src="/images/hero-1.jpg"
                            alt="Hero"
                            fill
                            style={{ objectFit: "cover" }}
                        />
                    </div>
                </div>                <div className="col-lg-4">
                    <p className="font-body">
                        Diam dolor diam ipsum et, tempor voluptua sit consetetur sit. Aliquyam diam amet diam et eos sadipscing labore. Clita erat ipsum et lorem et sit, sed stet no labore lorem sit. Sanctus clita duo justo et tempor consetetur takimata eirmod.
                    </p>
                    <p>
                        <i className={`bi bi-arrow-up animate-up-down ${styles.arrowIcon}`}></i>
                    </p>
                    <div className="position-relative">
                        <Image
                            className="img-fluid rounded"
                            src="/images/hero-3.jpg"
                            alt="Hero"
                            width={600}
                            height={400}
                            style={{ objectFit: "cover" }}
                        />
                    </div>
                </div>
            </div>

            {/* Hero End */}
        </div>

    );
}
export default HeroCard;