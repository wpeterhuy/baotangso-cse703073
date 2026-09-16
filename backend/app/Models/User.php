<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;

class User extends Authenticatable
{
    use HasFactory, Notifiable;

    protected $fillable = ['email', 'password_hash', 'role', 'status', 'last_login_at'];
    protected $hidden = ['password_hash'];
    protected $casts = ['last_login_at' => 'datetime'];

    public function getAuthPassword()
    {
        return $this->password_hash;
    }

    public function visitSessions()
    {
        return $this->hasMany(VisitSession::class);
    }

    public function guestbookEntries()
    {
        return $this->hasMany(GuestbookEntry::class);
    }

    public function collections()
    {
        return $this->hasMany(Collection::class);
    }

    public function auditLogs()
    {
        return $this->hasMany(AuditLog::class, 'actor_id');
    }
}
