# pyception
A more meaningful exception's collection for Python

* simple and lightweight library
* inspired on frameworks and languages such as .NET, javasdk, ruby, php etc.

Feel free to open a pull request!

Please, use [Jeremy Mack's](http://seesparkbox.com/foundry/semantic_commit_messages) commit style.

``` python

    import pyception

    if not user.has_previlege('admin'):
        raise pyception.security.PrivilegeNotHeldException('Not allowed.')

```
