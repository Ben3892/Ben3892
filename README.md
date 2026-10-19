# Ben (Jiangan) Yuan

大模型预训练算法工程师，关注 **大语言模型预训练与中训练、知识蒸馏、训练数据与评测、搜索 Agent**，以及分布式训练、高性能计算和大模型可解释性。

目前在百度搜索策略部参与 **100B 级 MoE 搜索大模型**的预训练与中训练，希望让大模型训练更高效、更可靠。

[个人主页](https://ben3892.github.io/)· [Google Scholar](https://scholar.google.com/citations?user=hUOpBWsAAAAJ) · [邮件联系](mailto:jianganyuan@link.cuhk.edu.cn)

## GitHub Stats and Activity

<p align="center">
  <a href="https://github.com/Ben3892">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github-stats-extended.vercel.app/api?username=Ben3892&amp;show_icons=true&amp;theme=github_dark&amp;hide_border=true&amp;rank_icon=github" />
      <img height="175" alt="Ben3892 GitHub stats: stars, commits, pull requests, issues and contributions" src="https://github-stats-extended.vercel.app/api?username=Ben3892&amp;show_icons=true&amp;theme=default&amp;hide_border=true&amp;rank_icon=github" />
    </picture>
  </a>
  <a href="https://github.com/Ben3892?tab=repositories">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github-stats-extended.vercel.app/api/top-langs/?username=Ben3892&amp;layout=compact&amp;langs_count=6&amp;theme=github_dark&amp;hide_border=true" />
      <img height="175" alt="Most used languages in Ben3892's public repositories" src="https://github-stats-extended.vercel.app/api/top-langs/?username=Ben3892&amp;layout=compact&amp;langs_count=6&amp;theme=default&amp;hide_border=true" />
    </picture>
  </a>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=Ben3892&amp;theme=github-compact&amp;hide_border=true&amp;area=true" />
  <img width="100%" alt="Ben3892 GitHub contribution activity over the last 31 days" src="https://github-readme-activity-graph.vercel.app/graph?username=Ben3892&amp;bg_color=ffffff&amp;color=24292f&amp;line=0969da&amp;point=0969da&amp;area_color=ddf4ff&amp;area=true&amp;hide_border=true" />
</picture>

## My Favorite Tools and Technologies

<p align="center">
  <a href="https://skillicons.dev">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=py,pytorch,cpp,linux,bash,git,github,docker&amp;theme=dark&amp;perline=8" />
      <img alt="Python, PyTorch, C++, Linux, Bash, Git, GitHub and Docker" src="https://skillicons.dev/icons?i=py,pytorch,cpp,linux,bash,git,github,docker&amp;theme=light&amp;perline=8" />
    </picture>
  </a>
</p>

<p align="center">
  <img alt="CUDA" src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&amp;logo=nvidia&amp;logoColor=white" />
  <img alt="Triton" src="https://img.shields.io/badge/Triton-2563EB?style=flat-square" />
  <img alt="Megatron-LM" src="https://img.shields.io/badge/Megatron--LM-76B900?style=flat-square&amp;logo=nvidia&amp;logoColor=white" />
  <img alt="verl" src="https://img.shields.io/badge/verl-7C3AED?style=flat-square" />
</p>

## 工作经历

### 百度 · 搜索策略部 | 2025.08 — 至今

从事大模型预训练与中训练，主要负责蒸馏目标设计、数学与代码数据策略、评测归因和搜索 Agent 数据合成。

- **预训练 off policy kd训练目标设计**：完成裁剪后模型的离线 Forward KL 恢复训练，在代表性评测上保留 Teacher 约 **90+%** 的能力；分析 Forward KL 与下一 Token 预测（NTP）在不同领域的能力权衡，设计领域条件目标路由，并在代理模型与目标模型上验证。
- **数学与代码数据**：搭建合成、质量过滤、知识规则约束、多答案投票与沙箱执行校验的数据流水线，形成约 **100B级别 Token** 的有效训练数据；通过等 Token 对照实验与错误归因持续改进数据质量。
- **搜索 Agent**：基于 Wikipedia、BM25、向量召回、重排与实体图合成多跳问题和搜索轨迹，将查询改写、证据定位与状态转移等能力拆解为原子任务，开展课程式中训练与细粒度评测。
- **后训练 off policy kd训练目标设计**： 针对业务落地场景的模型，进行跨词表蒸馏off policy目标设计，目标是为跨词表mopd进行warm up，提供更好的热启模型，对齐不同模型的分布。

### 字节跳动 · 飞书搜索团队 | 2024.07 — 2025.02

围绕企业知识问答场景开展模型 SFT 训练与效果优化，关注推理效率与工程可用性。

## 代表项目

| 项目 | 主要工作与成果 |
| --- | --- |
| [大模型蒸馏目标设计与规模化验证](https://ben3892.github.io/portfolio/llm-distillation-objectives/) | 比较 Forward KL 与 NTP 的领域差异，验证领域条件目标路由；进一步使用 1B Proxy 模型搜索 Top-k、Temperature 与损失权重等蒸馏配置。 |
| [数学与代码数据合成—过滤—评测闭环](https://ben3892.github.io/portfolio/math-code-data-pipeline/) | 结合知识点驱动合成、分领域过滤和错误归因。｜
| [搜索 Agent 多跳推理数据合成](https://ben3892.github.io/portfolio/search-agent-data-synthesis/) | 建立“检索构建—图上采样—轨迹合成—质量控制—能力评测”流程，自建原子能力 Benchmark，并结合后训练 SFT 与 BrowseComp 评估在线搜索能力。 |


## 教育经历

| 时间 | 学校 | 专业与学位 |
| --- | --- | --- |
| 2023.09 — 2025.07 | 香港中文大学（深圳） | 数据科学硕士 |
| 2019.09 — 2023.07 | 华南理工大学 | |

## 技术方向

- **模型训练**：LLM Pre-training、Mid-training、SFT、MoE、Knowledge Distillation、Forward KL、NTP。
- **数据与评测**：数据合成、质量过滤、沙箱校验、能力评测与错误归因、课程学习。
- **检索与 Agent**：BM25、Embedding、Reranking、实体图、多跳推理、Query Reformulation、Evidence Grounding。
- **训练系统**：分布式训练、CUDA、Triton、Kernel Fusion。

## 阅读与分享

持续整理大模型训练与系统相关笔记，包括 Megatron-LM、verl 源码阅读，以及 Attention 机制、Attention Sink 和技术报告阅读。

## Contribution Snake

<!-- .github/workflows/snake.yml 每天生成动画并发布到 output 分支；首次推送到 main 后自动生成。 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Ben3892/Ben3892/output/github-contribution-grid-snake-dark.svg" />
  <img width="100%" alt="Animated snake following Ben3892's GitHub contribution calendar" src="https://raw.githubusercontent.com/Ben3892/Ben3892/output/github-contribution-grid-snake.svg" />
</picture>

欢迎围绕大模型训练、知识蒸馏、预训练数据与可解释性交流：**[jianganyuan@link.cuhk.edu.cn](mailto:jianganyuan@link.cuhk.edu.cn)**。
