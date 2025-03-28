<template>
    <div class="mybook-section">
      <div class="column">
        <h3>Read Online Anywhere</h3>
        <h5>Modern Literature and Classics</h5>
        <p>
          Online Book is a convenient platform for reading e-books online. Our library contains thousands of works across different genres: from classical literature to modern bestsellers. You'll find detective stories, science fiction, fantasy, romance, business books, psychology, and children's literature. Our collection is constantly updated with new works. Many books are available for free, including classical literature and works by emerging authors.
        </p>
        <h5>Flexible Access Options</h5>
        <p>
          We offer various access options to the library. Choose a basic plan for access to the main collection or a premium subscription for full access to all books. Different subscription periods are available: monthly, semi-annual, or yearly. Read as many books as you want without additional costs. Try different works and find what truly resonates with you.
        </p>
        <h5>Convenient Browser Reading</h5>
        <p>
          Online Book is designed for comfortable reading right in your browser. The adaptive design allows reading on any device: computer, tablet, or smartphone. Customize font size, color scheme, and other parameters to your liking. The service works even in offline mode: just open a book once while connected to the internet, and it will be saved in your browser cache for further reading.
        </p>
      </div>

      <div class="column">
        <h3>Additional Features</h3>
        <h5>Reading Progress Saving</h5>
        <p>
          Our service automatically saves your reading progress across all devices. Start reading on your home computer and continue from the same place on your smartphone. Create bookmarks, highlight important quotes, and take notes — everything syncs in your account. Export your notes and quotes in a convenient format for future use.
        </p>
        <h5>Reading Progress Tracking</h5>
        <p>
          Monitor your reading achievements through personal statistics. Track the number of pages read, reading time, and completed books. Receive weekly reports on your activity and set new goals for developing reading skills.
        </p>
        <h5>Smart Recommendations</h5>
        <p>
          In Online Book, you'll find thematic book collections for every taste. Our recommendation system considers your preferences and suggests books that might interest you. Discover new authors, explore different genres, and find books on current topics. The regularly updated recommendations section helps you stay informed about literary novelties and find interesting reads.
        </p>
      </div>
    </div>
</template>
  
  <script>
  export default {
    name: "MyBookSection"
  };
  </script>
  
  <style scoped>
  .mybook-section {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    gap: 20px;
    padding: 20px;
    font-family: 'Roboto', sans-serif;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .column {
    width: 45%;
    padding: 15px;
  }
  
  h2, h3, h5 {
    color: #333;
  }
  
  p {
    font-size: 13px;
    color: #555;
    line-height: 1.7;
    margin-bottom: 15px;
  }
  
  h3 {
    margin-top: 20px;
  }
  
  h5 {
    margin-top: 15px;
    color: #444;
  }
  
  p {
    text-align: justify;
  }
  </style>
