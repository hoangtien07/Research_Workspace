# Research Workspace — Claude context

> File này được Claude Code tải tự động từ **mọi repo** trong workspace vì `Research/` là thư mục cha
> chung. Đọc trước khi làm bất kỳ việc gì. Chi tiết từng repo trong CLAUDE.md của repo đó.

---

## Chương trình nghiên cứu

**DiSC × Driver-gene** — lần đầu áp dụng khung DiSC (4 chiều behavioral: D/I/S/C) như một không gian
đặc trưng chức năng gene, tích hợp với lý thuyết mạng phức hợp để phân tích hệ gene điều khiển người.

- **Tác giả**: Phạm Hoàng Tiến (PhD candidate, corresponding); Trần Tiến Dũng (Supervisor)
- **Anchor**: Drivergene.net — Pham & Tran 2024, peer-reviewed, supervisor's prior work
- **Target**: Briefings in Bioinformatics (Q1, IF ≈ 9.5); backup: CBM / PLOS Comp Biol
- **Submission**: 2026-08-23

---

## Cấu trúc workspace (hub-and-spoke)

```
Research/                    ← meta-repo  (hoangtien07/Research_Workspace)
├── shared/                  ← hub        (hoangtien07/research_shared)
│   ├── CLAUDE.md            ← hub-specific rules
│   ├── ddl-pipeline/        ← pip-installable shared Python package  (v0.1.0)
│   ├── scripts/             ← cross-paper CLI tools
│   └── .claude/             ← SOURCE OF TRUTH: commands, hooks, settings
└── paper-disc-grn/          ← spoke      (hoangtien07/paper-disc-grn, private)
    ├── CLAUDE.md            ← paper-specific rules
    ├── about-project.md     ← scientific thesis + experimental design
    └── .claude/             ← copy từ hub; sync: python shared/scripts/sync_claude.py paper-disc-grn
```

**Nguyên tắc:**
- Hub sở hữu mọi shared code (`ddl-pipeline`) và tooling (`.claude/`).
- Spoke sở hữu manuscript, data, results, pipeline scripts riêng.
- Spokes import hub: `from ddl_pipeline.X import Y` (không duplicate code).

---

## Quy tắc áp dụng mọi nơi

1. **Không bao giờ bịa số liệu.** Mọi con số (Q, p-value, AUC, N, %) phải truy ra được đến file trong
   `results/` hoặc `data/processed/`. Nếu không chắc → viết `[CHECK: source?]`.
2. **Không bao giờ bịa citation.** Chỉ dùng BibTeX key đã có trong `references.bib`.
   Nếu thiếu → dùng `/add-ref <DOI>` trước.
3. **`ddl-pipeline` là source of truth cho shared analysis code.** Nếu hai spoke cần cùng một hàm →
   thêm vào package, không viết lại trong `src/` của spoke.
4. **Build artifacts** (`build/`, `*.docx`, `__pycache__/`) là gitignored — không commit.
5. **Không sửa `paper_DiSC/`** — đây là draft cũ đã archive (2026-04-20), bị thay thế bởi
   `paper-disc-grn`. Không cite, không reference.

---

## Khung DiSC

| Chiều | Ký hiệu | Ý nghĩa sinh học |
|---|---|---|
| Dominance (D) | x_D | Hub/trung tâm: regulation, control, broad connectivity |
| Influence (I) | x_I | Signaling: communication, pathway activation |
| Steadiness (S) | x_S | Structural: maintenance, scaffolding, stability |
| Conscientiousness (C) | x_C | Specialised function: metabolic/biosynthetic roles |

**DiSC vector**: `F(gene) → [x_D, x_I, x_S, x_C] ∈ [0,1]⁴`, L1-normalised (Σ = 1).  
**Current version**: `disc_weights_v3` — fixes Bug-K, Bug-Sub, Bug-Word, Bug-TF.  
**Import**: `from ddl_pipeline.disc_weights_v3 import score_term`

---

## Navigation — tìm thông tin ở đâu

| Cần thông tin về | Tài liệu |
|---|---|
| Hub conventions, ddl-pipeline, slash commands | `shared/CLAUDE.md` |
| DiSC-GRN paper: journal, word budget, writing rules | `paper-disc-grn/CLAUDE.md` |
| Scientific thesis, hypotheses, experimental design | `paper-disc-grn/about-project.md` |
| Execution plan: H1–H4 round-by-round | `~/.claude/plans/thi-t-k-tier-n-groovy-feather.md` |
| Monorepo migration plan | `~/.claude/plans/l-n-k-ho-ch-concurrent-kahn.md` |
| ddl-pipeline changelog | `shared/CHANGELOG.md` |

---

## Slash commands

Commands sẵn có khi làm việc trong bất kỳ repo nào (via `.claude/commands/`):

| Command | Tác dụng |
|---|---|
| `/verify-citations` | Kiểm tra mọi `[@key]` resolve trong `references.bib` |
| `/verify-numbers` | Đối chiếu số liệu trong manuscript với CSVs |
| `/paper-status` | Word count, citations, figures, open `[CHECK:]` markers |
| `/build-paper [target]` | verify + pandoc → `build/manuscript.docx` |
| `/add-ref <DOI>` | Fetch BibTeX entry by DOI → append `references.bib` |
| `/new-paper <slug>` | Scaffold `paper-<slug>/` từ `paper_template` |
| `/audit-paper` | Full pre-submission audit với go/no-go verdict |

---

## Venv và Python

```bash
# Hub venv (dùng chung cho mọi spoke khi chưa có spoke venv riêng):
shared/.venv/Scripts/python.exe

# Spoke-local (nếu đã setup):
paper-disc-grn/.venv/Scripts/python.exe

# Kiểm tra ddl-pipeline:
python -c "from ddl_pipeline.disc_weights_v3 import score_term; print('ok')"
```
