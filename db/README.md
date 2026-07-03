# テーブル構造
## blogsテーブル
| カラム名 | 型 |
| -- | -- |
| `id` | `INTEGER` |
| `blog_url` | `TEXT` |
| `created_at` | `TEXT` |
| `updated_at` | `TEXT` |

`id` は一意であり、`auto_increment` であり、主キーである。

`blog_url, created_at, updatd_at` は `null` を許容しない。

## imagesテーブル
| カラム名 | 型 |
| -- | -- |
| `id` | `INTEGER` |
| `blog_id` | `TEXT` |
| `url` | `TEXT` |
| `created_at` | `TEXT` |
| `updated_at` | `TEXT` |

`id` は一意であり、`auto_increment` であり、主キーである。

`blog_id, url, created_at, updatd_at` は `null` を許容しない。

`blog_id` は `blogs` テーブルの `id` である。
