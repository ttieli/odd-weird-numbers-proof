# RavenThought 项目记忆

## 会话记录

### 2026-03-09 17:30:00 (会话ID: r7k2)

#### 完成 ✅

- 调研 Antigravity IDE 文生图能力，确认支持 Nano Banana Pro / Nano Banana 2 生成 App Icon 和 Logo
- 撰写完整中文使用手册 `daily/20260305/topics/20260305_Antigravity文生图使用手册.md`
  - 两条路径：Antigravity IDE（可视化）和 Gemini CLI nanobanana 扩展（终端）
  - CLI `/icon` 命令支持批量多尺寸导出、透明背景、圆角、多风格
  - Gemini Pro 用户配额每 5 小时刷新，支持 4K
  - 用户后续实测补充了避坑章节（API Key 继承失效、Agent Policy 限制、非标准 CLI 参数等）
- 处理小红书分享：Neo（4ier/neo）— 让 AI Agent 直接调用任何网站的 API
  - 创建课题文档 `daily/20260305/topics/20260305_Neo_API抓取Agent工具.md`
  - 包含完整安装步骤、40+ CLI 命令参考、4 个典型工作流、架构图、工具对比
  - 关联 HandOff_HandOn、Skills-Factory、Xiaojin_EDMP
- 更新 `daily/20260305/20260305_每日汇总.md` 共 3 条课题记录

#### 未完成 ⏸️

（无）

#### 问题 ⚠️

- Gemini CLI nanobanana 扩展实测存在多个坑：API Key 继承失效、Agent Policy 限制、/icon 等命令只能在交互模式内使用。结论是追求成功率建议用 Antigravity IDE。

#### 备注 💡

- 本次会话跨日期（03-05 开始调研，03-09 保存进度），文档均记录在 20260305 日期目录下
- Neo 项目的 `export-skill` 功能与 Skills-Factory 高度契合，值得后续深入集成
