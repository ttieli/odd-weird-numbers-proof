# RavenThought 项目记忆

## 会话记录

### 2026-03-20 16:35:00 (会话ID: bu8f)

#### 完成 ✅

- **瓦良格号航母购买始末深度调研** → `daily/20260320/topics/20260320_瓦良格号航母购买始末.md`
  - 资金来自华夏证券（邵淳决策）→ 徐增平挪用专款 → 国家以8.78亿接手
  - 补充华夏证券破产史、朱镕基批示背景、邵淳非红二代分析
- **臧伟履历调研** → `daily/20260320/topics/20260320_臧伟履历调研.md`
  - 6个信源确认身份（教育部校外培训监管司应急指导处处长）
  - 发现延边大学医学部挂职线索（百度学术，2017-2020论文）
  - 个人履历公开渠道无法获取
- 更新每日汇总，共3条课题

#### 未完成 ⏸️

- 臧伟个人履历（出生年份、学历、毕业院校）需内部渠道

#### 备注 💡

- 百度搜索对中国公务员信息最有效；Chrome浏览器自动化用于突破wf编码问题
- 延边大学挂职线索由用户提示发现

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
