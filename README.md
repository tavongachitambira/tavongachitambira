<!-- Palette: Teal #004741 / Sand #F0EDE4 (matches tavongachitambira.vercel.app) -->

<p align="center">
  <img width="100%" src="assets/hero.svg" alt="Welcome to my GitHub. Hi, I'm Tavonga Chitambira. Full Stack Engineer, ML Engineer." />
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=tavongachitambira&label=Profile+views&color=004741&style=for-the-badge" alt="Profile views" />
</p>

<p align="center">
  <a href="https://tavongachitambira.vercel.app"><img src="https://img.shields.io/badge/View_my_portfolio-004741?style=for-the-badge&logo=vercel&logoColor=F0EDE4" alt="Portfolio" /></a>
  <a href="https://tavongachitambira.vercel.app/resume.pdf"><img src="https://img.shields.io/badge/Download_r%C3%A9sum%C3%A9-F0EDE4?style=for-the-badge&logo=readdotcv&logoColor=004741" alt="Resume" /></a>
</p>

---

## 🧑‍💻 About me

I'm a software engineer specializing in **production Machine Learning systems** and **real-time web apps**, from training and deploying models to shipping the interfaces, APIs, and infrastructure that serve them. I care about the architectural decisions that separate a system that holds up from one that collapses under load.

- 🎓 B.Sc. Computer Science at Vishwakarma University, Pune
- 🚧 Currently shipping **SyncBoard**, a multiplayer incident platform
- 📚 Learning cloud **MLOps**, **PyTorch**, **LLMs & RAG**, **Kubernetes**
- 🏀 Basketball · ♟️ Chess
- 🤝 Open to collaborating on interesting problems

---

## 🔨 Currently building

### SyncBoard <sub>`in development`</sub>

Real-time multiplayer incident management workspace. Think PagerDuty meets Notion.

- Horizontally scaled **Socket.io** cluster bridged via **Redis Pub/Sub**
- **Yjs CRDT** collaborative editing with optimistic locking and 409 rollback
- **Stripe** usage metering through **BullMQ**, kept off the socket hot path
- RS256 JWT auth with refresh-token rotation in Redis, no auth library
- Strict tenant isolation: cross-tenant requests return 404, never 403

<img src="https://img.shields.io/badge/Next.js-004741?style=flat-square&logo=nextdotjs&logoColor=F0EDE4" /> <img src="https://img.shields.io/badge/Socket.io-004741?style=flat-square&logo=socketdotio&logoColor=F0EDE4" /> <img src="https://img.shields.io/badge/Yjs-004741?style=flat-square" /> <img src="https://img.shields.io/badge/Redis-004741?style=flat-square&logo=redis&logoColor=F0EDE4" /> <img src="https://img.shields.io/badge/PostgreSQL-004741?style=flat-square&logo=postgresql&logoColor=F0EDE4" /> <img src="https://img.shields.io/badge/BullMQ-004741?style=flat-square" /> <img src="https://img.shields.io/badge/Stripe-004741?style=flat-square&logo=stripe&logoColor=F0EDE4" /> <img src="https://img.shields.io/badge/Kubernetes-004741?style=flat-square&logo=kubernetes&logoColor=F0EDE4" />

**Next:** ML inside SyncBoard: incident auto-classification, runbook RAG lookup, on-call summarisation.

---

## 🧰 Tech stack

<table>
  <tr>
    <td width="120"><b>Frontend</b></td>
    <td>
      <img src="https://img.shields.io/badge/TypeScript-004741?style=for-the-badge&logo=typescript&logoColor=F0EDE4" alt="TypeScript" />
      <img src="https://img.shields.io/badge/Next.js-004741?style=for-the-badge&logo=nextdotjs&logoColor=F0EDE4" alt="Next.js" />
      <img src="https://img.shields.io/badge/React-004741?style=for-the-badge&logo=react&logoColor=F0EDE4" alt="React" />
      <img src="https://img.shields.io/badge/Tailwind_CSS-004741?style=for-the-badge&logo=tailwindcss&logoColor=F0EDE4" alt="Tailwind CSS" />
      <img src="https://img.shields.io/badge/Framer_Motion-004741?style=for-the-badge&logo=framer&logoColor=F0EDE4" alt="Framer Motion" />
      <img src="https://img.shields.io/badge/shadcn/ui-004741?style=for-the-badge&logo=shadcnui&logoColor=F0EDE4" alt="shadcn/ui" />
      <img src="https://img.shields.io/badge/Apollo_Client-004741?style=for-the-badge&logo=apollographql&logoColor=F0EDE4" alt="Apollo Client" />
    </td>
  </tr>
  <tr>
    <td width="120"><b>Backend</b></td>
    <td>
      <img src="https://img.shields.io/badge/Node.js-004741?style=for-the-badge&logo=nodedotjs&logoColor=F0EDE4" alt="Node.js" />
      <img src="https://img.shields.io/badge/GraphQL-004741?style=for-the-badge&logo=graphql&logoColor=F0EDE4" alt="GraphQL" />
      <img src="https://img.shields.io/badge/Prisma-004741?style=for-the-badge&logo=prisma&logoColor=F0EDE4" alt="Prisma" />
      <img src="https://img.shields.io/badge/PostgreSQL-004741?style=for-the-badge&logo=postgresql&logoColor=F0EDE4" alt="PostgreSQL" />
      <img src="https://img.shields.io/badge/Redis-004741?style=for-the-badge&logo=redis&logoColor=F0EDE4" alt="Redis" />
      <img src="https://img.shields.io/badge/Socket.io-004741?style=for-the-badge&logo=socketdotio&logoColor=F0EDE4" alt="Socket.io" />
      <img src="https://img.shields.io/badge/BullMQ-004741?style=for-the-badge&logo=bullmq&logoColor=F0EDE4" alt="BullMQ" />
    </td>
  </tr>
  <tr>
    <td width="120"><b>Data &amp; Ml</b></td>
    <td>
      <img src="https://img.shields.io/badge/Python-004741?style=for-the-badge&logo=python&logoColor=F0EDE4" alt="Python" />
      <img src="https://img.shields.io/badge/pandas-004741?style=for-the-badge&logo=pandas&logoColor=F0EDE4" alt="pandas" />
      <img src="https://img.shields.io/badge/scikit--learn-004741?style=for-the-badge&logo=scikitlearn&logoColor=F0EDE4" alt="scikit-learn" />
      <img src="https://img.shields.io/badge/Power_BI-004741?style=for-the-badge&logo=powerbi&logoColor=F0EDE4" alt="Power BI" />
      <img src="https://img.shields.io/badge/Tableau-004741?style=for-the-badge&logo=tableau&logoColor=F0EDE4" alt="Tableau" />
      <img src="https://img.shields.io/badge/PyTorch-004741?style=for-the-badge&logo=pytorch&logoColor=F0EDE4" alt="PyTorch" />
    </td>
  </tr>
  <tr>
    <td width="120"><b>Tooling</b></td>
    <td>
      <img src="https://img.shields.io/badge/Git-004741?style=for-the-badge&logo=git&logoColor=F0EDE4" alt="Git" />
      <img src="https://img.shields.io/badge/GitHub-004741?style=for-the-badge&logo=github&logoColor=F0EDE4" alt="GitHub" />
      <img src="https://img.shields.io/badge/Linux-004741?style=for-the-badge&logo=linux&logoColor=F0EDE4" alt="Linux" />
      <img src="https://img.shields.io/badge/Docker-004741?style=for-the-badge&logo=docker&logoColor=F0EDE4" alt="Docker" />
      <img src="https://img.shields.io/badge/Kubernetes-004741?style=for-the-badge&logo=kubernetes&logoColor=F0EDE4" alt="Kubernetes" />
      <img src="https://img.shields.io/badge/Turborepo-004741?style=for-the-badge&logo=turborepo&logoColor=F0EDE4" alt="Turborepo" />
    </td>
  </tr>
</table>

<sub>🌱 Currently learning: PyTorch · LLMs & RAG · Kubernetes</sub>

---

## 📊 GitHub stats

<p align="center">
  <img height="170" alt="GitHub stats" src="https://github-readme-stats.vercel.app/api?username=tavongachitambira&show_icons=true&hide_border=true&bg_color=004741&title_color=F0EDE4&text_color=F0EDE4&icon_color=7FD1C7&border_radius=14" />
  <img height="170" alt="Top languages" src="https://github-readme-stats.vercel.app/api/top-langs/?username=tavongachitambira&layout=compact&hide_border=true&bg_color=004741&title_color=F0EDE4&text_color=F0EDE4&border_radius=14" />
</p>

<p align="center">
  <img alt="Contribution graph" src="https://raw.githubusercontent.com/tavongachitambira/tavongachitambira/output/contribution-card.svg" width="100%" />
</p>

---

## 📫 Let's connect

<p align="center">
  <a href="mailto:obichitas03@gmail.com"><img src="https://img.shields.io/badge/Email-004741?style=for-the-badge&logo=gmail&logoColor=F0EDE4" alt="Email" /></a>
  <a href="https://www.linkedin.com/in/tavonga-chitambira-213745309/"><img src="https://img.shields.io/badge/LinkedIn-004741?style=for-the-badge&logo=linkedin&logoColor=F0EDE4" alt="LinkedIn" /></a>
  <a href="https://tavongachitambira.vercel.app"><img src="https://img.shields.io/badge/Portfolio-004741?style=for-the-badge&logo=vercel&logoColor=F0EDE4" alt="Portfolio" /></a>
  <a href="https://www.instagram.com/obi_chitas03/"><img src="https://img.shields.io/badge/Instagram-004741?style=for-the-badge&logo=instagram&logoColor=F0EDE4" alt="Instagram" /></a>
</p>

<p align="center"><sub>✉️ obichitas03@gmail.com · 📍 Pune, India</sub></p>

<img width="100%" src="assets/footer.svg" alt="" />
