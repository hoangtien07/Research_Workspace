# Research Workspace

> Tải tự động từ **mọi repo** vì `Research/` là cha chung. Đọc đầu tiên. Chi tiết từng repo trong CLAUDE.md của repo đó.

## Dự án

**DiSC × Driver-gene** — lần đầu áp dụng khung DiSC (D/I/S/C) như không gian đặc trưng chức năng gene trên mạng GRN người.

- **Tác giả**: Phạm Hoàng Tiến (PhD, corresponding); Trần Tiến Dũng (Supervisor)
- **Anchor**: Drivergene.net — Pham & Tran 2024 (supervisor's peer-reviewed work)
- **Target**: Briefings in Bioinformatics (Q1, IF ≈ 9.5); submission 2026-08-23

## Cấu trúc

```
Research/                        (hoangtien07/Research_Workspace)
├── .claude/                 ← tooling duy nhất: commands, hooks, agents, settings
├── shared/                      (hoangtien07/research_shared)
│   ├── ddl-pipeline/        ← pip package, v0.1.0
│   └── scripts/             ← verify-*, paper-status, new-paper, sync-claude
└── paper-disc-grn/              (hoangtien07/paper-disc-grn, private)
    └── .claude/settings.json ← hooks pointing to ../.claude/ (standalone support)
```

## Quy tắc bất biến

1. **Không bịa số.** Mọi con số → phải truy được đến `results/` hoặc `data/processed/`. Nếu không chắc → `[CHECK: source?]`.
2. **Không bịa citation.** Chỉ dùng key có trong `references.bib`. Thiếu → `/add-ref <DOI>` trước.
3. **`ddl-pipeline` là source of truth** cho shared code. Import: `from ddl_pipeline.X import Y`. Không duplicate vào `src/` của spoke.
4. **Không commit** `build/`, `*.docx`, `__pycache__/`.
5. **`paper_DiSC/`** là draft cũ đã archive (2026-04-20) — không cite, không sửa.

## Khung DiSC

`F(gene) → [x_D, x_I, x_S, x_C] ∈ [0,1]⁴` (L1-normalised). Version hiện tại: `disc_weights_v3`.

| x_D | x_I | x_S | x_C |
|---|---|---|---|
| Hub/regulation | Signaling | Structural | Specialised |

## Navigation

| Cần | Đọc |
|---|---|
| Hub: ddl-pipeline, scripts | `shared/CLAUDE.md` |
| Paper: journal, writing rules | `paper-disc-grn/CLAUDE.md` |
| Scientific thesis | `paper-disc-grn/about-project.md` |
| Execution plan (H1–H4) | `~/.claude/plans/thi-t-k-tier-n-groovy-feather.md` |
