import React from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

// 🔥 Direct SVG imports (cleaner than require)
import QIDocsSocial from '@site/static/img/qidocssocial.svg';
import QIDocsHearts from '@site/static/img/qidocshearts.svg';
import QIDocsPage from '@site/static/img/qidocspage.svg';

const FeatureList = [
  {
    title: 'Easy to Use',
    Svg: QIDocsSocial,
    description: (
      <>
        QiDocs was designed from the ground up as a QiLife module to quickly organize QiNotes and restore clarity in your digital world.
      </>
    ),
  },
  {
    title: 'Focus on What Matters',
    Svg: QIDocsHearts,
    description: (
      <>
        Move your chaos into order. QiDocs helps you build a calm, navigable brain that grows with you, not against you.
      </>
    ),
  },
  {
    title: 'Powered by React',
    Svg: QIDocsPage,
    description: (
      <>
        Extend or customize your system with full control. Docusaurus gives you a stable foundation — QiLife takes it quantum.
      </>
    ),
  },
];

function Feature({ Svg, title, description }) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
