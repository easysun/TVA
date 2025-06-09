import { useState } from 'react';
import styles from '../styles/Home.module.css';

interface FAQ {
  question: string;
  answer: string;
}

const faqData: FAQ[] = [
  {
    question: 'What is TVA Time Authority?',
    answer:
      'A decentralized application on Solana that ensures the preservation of historical data with cryptographic proofs.',
  },
  {
    question: 'How do I submit a historical record?',
    answer:
      'Use the frontend form to submit your historical version. The backend AI will validate and the smart contract will store it on-chain.',
  },
];

export default function Home() {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>TVA Time Authority FAQ</h1>
      <div className={styles.faq}>
        {faqData.map((item) => (
          <div key={item.question} className={styles.item}>
            <h2 className={styles.question}>{item.question}</h2>
            <p className={styles.answer}>{item.answer}</p>
          </div>
        ))}
      </div>
    </div>
  );
}