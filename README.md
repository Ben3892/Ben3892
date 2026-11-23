# Ben (Jiangan) Yuan

大模型预训练算法工程师，关注 **大语言模型预训练与中训练、知识蒸馏、训练数据与评测、搜索 Agent**，以及分布式训练、高性能计算和大模型可解释性。

目前在百度搜索策略部参与 **100B 级 MoE 搜索大模型**的预训练与中训练，希望让大模型训练更高效、更可靠。

[个人主页](https://ben3892.github.io/) · [Google Scholar](https://scholar.google.com/citations?user=hUOpBWsAAAAJ) · [邮件联系](mailto:jianganyuan@link.cuhk.edu.cn)

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
  <source media="(prefers-color-scheme: dark)" srcset="assets/github-activity-dark.svg" />
  <img width="100%" alt="Ben3892 GitHub contribution activity over the last 31 days" src="assets/github-activity.svg" />
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

- **预训练与中训练蒸馏目标**：完成裁剪后模型的离线 Forward KL 恢复训练，在代表性评测上保留 Teacher 约 **90+%** 的能力；分析 Forward KL 与下一 Token 预测（NTP）在不同领域的能力权衡，设计领域条件目标路由，并在代理模型与目标模型上验证。
- **数学与代码数据**：搭建合成、质量过滤、知识规则约束、多答案投票与沙箱执行校验的数据流水线，形成约 **100B级别 Token** 的有效训练数据；通过等 Token 对照实验与错误归因持续改进数据质量。
- **搜索 Agent**：基于 Wikipedia、BM25、向量召回、重排与实体图合成多跳问题和搜索轨迹，将查询改写、证据定位与状态转移等能力拆解为原子任务，开展课程式中训练与细粒度评测。
- **后训练跨词表蒸馏**：设计 off-policy KD 目标，对齐不同模型的输出分布，为跨词表 MOPD 提供热启模型。

## 代表项目

| 项目 | 主要工作与成果 |
| --- | --- |
| [大模型蒸馏目标设计与规模化验证](https://ben3892.github.io/portfolio/llm-distillation-objectives/) | 比较 Forward KL 与 NTP 的领域差异，验证领域条件目标路由；进一步使用 1B Proxy 模型搜索 Top-k、Temperature 与损失权重等蒸馏配置。 |
| [数学与代码数据合成—过滤—评测闭环](https://ben3892.github.io/portfolio/math-code-data-pipeline/) | 结合知识点驱动合成、分领域过滤和错误归因，通过等 Token 对照实验区分数据规模与质量收益。 |
| [搜索 Agent 多跳推理数据合成](https://ben3892.github.io/portfolio/search-agent-data-synthesis/) | 建立“检索构建—图上采样—轨迹合成—质量控制—能力评测”流程，自建原子能力 Benchmark，并结合后训练 SFT 与 BrowseComp 评估在线搜索能力。 |


## 开源项目与近期进展

| 项目 | 当前实现与验证范围 |
| --- | --- |
| [data_evaluation_loop](https://github.com/Ben3892/data_evaluation_loop) | 将能力切片、题级结果、`first_error` / `primary_error`、重复作答和正确性迁移组织为诊断闭环；已接入 AIME 整数答案规范化、离线判分与 `pass@k`。过程错误来自显式标注，fixture 用于验证接口与统计。 |
| [nano_model_experiment_framework](https://github.com/Ben3892/nano_model_experiment_framework) | 统一最小预训练与 SFT 入口，支持 PyTorch、Pai-Megatron-Patch 及带验证器的递归 SFT；已合并 A800 单卡/双卡 DP smoke 脚本与原生 Megatron checkpoint rollout。PyTorch CPU 合成实验已有记录，真实 A800 验收待完成；verl/OPD 为后续计划。 |
| [search_agent_environment](https://github.com/Ben3892/search_agent_environment) | 提供 BM25、Embedding/FAISS 与重排的离线检索服务，以及 `/search`、`/search_chunks`、`/visit` 接口和部署说明；完整 GPU 链路仍需在目标环境验证。 |

近期合并：**2026-11-20**，AIME 判分与 `pass@k`；**2026-11-23**，A800 验收脚本与 Megatron RSI 接入。详见各项目的公开代码与说明。

## 教育经历

| 时间 | 学校 |
| --- | --- |
| 2023.09 — 2025.07 | 香港中文大学（深圳） |
| 2019.09 — 2023.07 | 华南理工大学 |

## 技术方向

- **模型训练**：LLM Pre-training、Mid-training、SFT、MoE、Knowledge Distillation、Forward KL、NTP。
- **数据与评测**：数据合成、质量过滤、沙箱校验、能力评测与错误归因、课程学习。
- **检索与 Agent**：BM25、Embedding、Reranking、实体图、多跳推理、Query Reformulation、Evidence Grounding。
- **训练系统**：分布式训练、CUDA、Triton、Kernel Fusion。

## 阅读与分享

持续整理大模型训练与系统相关笔记，包括 Megatron-LM、verl 源码阅读，以及 Attention 机制、Attention Sink 和技术报告阅读。

## Contribution Snake

<!-- .github/workflows/snake.yml 每天更新 assets 中的活跃度图和贡献动画。 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/github-contribution-grid-snake-dark.svg" />
  <img width="100%" alt="Animated snake following Ben3892's GitHub contribution calendar" src="assets/github-contribution-grid-snake.svg" />
</picture>

欢迎围绕大模型训练、知识蒸馏、预训练数据与可解释性交流：**[jianganyuan@link.cuhk.edu.cn](mailto:jianganyuan@link.cuhk.edu.cn)**。
