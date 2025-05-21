import React from 'react';
import styles from './SpinnerCard.module.css';


interface SpinnerCardProps {
  showSpinner: boolean;
}

const SpinnerCard: React.FC<SpinnerCardProps> = ({ showSpinner }) => {
  return (
    <>
      {showSpinner && (
        <div className={`show bg-dark position-fixed translate-middle w-100 vh-100 top-50 start-50 d-flex align-items-center justify-content-center ${styles.spinnerContainer}`}>
          <div className={`spinner-border text-primary ${styles.spinner}`} role="status"></div>
        </div>
      )}
    </>
  );
};

export default SpinnerCard;
