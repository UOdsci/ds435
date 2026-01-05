
- [formulaic](https://matthewwardrop.github.io/formulaic)

## Pandas

Starting with v3, pandas will use
[Copy-On-Write](https://pandas.pydata.org/docs/dev/user_guide/copy_on_write.html),
which is a step towards sane data management
(see [here](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-view-versus-copy)
for context).
We recommend, and are using in course code, setting
```
pd.options.mode.copy_on_write = True
```
*Note:* confusing aspects of memory management remain.
For instance, previously
```
df.x[0] = 123
```
set the first element of column `x` to `123`
and produced a `SettingWithCopyWarning`.
Now, this operation **silently does nothing**.
But, this is in development, so perhaps it will change?


